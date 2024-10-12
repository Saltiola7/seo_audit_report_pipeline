import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote_plus
import duckdb
import logging
from concurrent.futures import ThreadPoolExecutor

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(env_path)

# Define the output directory for JSON files
OUTPUT_DIR = Path('/Users/tis/foam/github/leadata/sf_crawl/data/output')

def get_pagespeed_insights(url, strategy):
    api_key = os.getenv('PAGESPEED_INSIGHTS_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Ensure PAGESPEED_INSIGHTS_API_KEY is set in the .env file.")
    
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    encoded_url = quote_plus(url)
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={encoded_url}&strategy={strategy}&key={api_key}"
    
    logging.info(f"Fetching PageSpeed Insights data for {url} ({strategy})...")
    response = requests.get(api_url)
    
    if response.status_code == 200:
        logging.info(f"Successfully retrieved data for {url} ({strategy}).")
        return response.json()
    else:
        error_message = f"Failed to retrieve data for {url} ({strategy}). Status code: {response.status_code}"
        try:
            error_details = response.json()
            error_message += f"\nError details: {json.dumps(error_details, indent=2)}"
        except json.JSONDecodeError:
            error_message += f"\nResponse text: {response.text}"
        logging.error(error_message)
        return {"error": error_message}

def save_to_json(data, filename):
    # Construct the full output path using OUTPUT_DIR
    output_path = OUTPUT_DIR / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logging.info(f"JSON data saved to: {output_path}")

def append_to_duckdb(data, url):
    conn = duckdb.connect('/Users/tis/foam/github/seo_audit_reports/sources/seo/crawl.duckdb')
    audit_data = data['lighthouseResult']['audits']

    try:
        third_party_code = float(audit_data['third-party-summary']['details']['summary']['wastedMs'])
    except KeyError:
        third_party_code = None

    row_data = {
        'url': url,
        'fcp': int(audit_data['first-contentful-paint']['numericValue']),
        'lcp': int(audit_data['largest-contentful-paint']['numericValue']),
        'cls': float(audit_data['cumulative-layout-shift']['numericValue']),
        'speed_index': int(audit_data['speed-index']['numericValue']),
        'tti': int(audit_data['interactive']['numericValue']),
        'tbt': int(audit_data['total-blocking-time']['numericValue']),
        'performance_score': float(data['lighthouseResult']['categories']['performance']['score']),
        'viewport_score': int(audit_data['viewport']['score']),
        'render_blocking_resources': int(audit_data['render-blocking-resources']['numericValue']),
        'lcp_element': sum(int(item['timing']) for item in audit_data['largest-contentful-paint-element']['details']['items'][1]['items'] 
                           if item['phase'] in ["TTFB", "Load Delay", "Render Delay"]),
        'third_party_code': third_party_code,
        'javascript_execution_time': float(audit_data['bootup-time']['details']['summary']['wastedMs']),
        'main_thread_work': int(audit_data['mainthread-work-breakdown']['numericValue']),
        'unused_css': int(audit_data['unused-css-rules']['numericValue']),
        'modern_image_formats': int(audit_data['modern-image-formats']['numericValue']),
        'unminified_css': int(audit_data['unminified-css']['numericValue']),
        'image_optimization': int(audit_data['uses-optimized-images']['numericValue']),
        'unsized_images': len(audit_data['unsized-images']['details']['items']),
        'responsive_images': int(audit_data['uses-responsive-images']['score'])
    }

    columns = ', '.join(row_data.keys())
    values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) if v is not None else 'NULL' for v in row_data.values()])

    conn.execute(f"""
        INSERT INTO pagespeed_mobile ({columns})
        VALUES ({values})
    """)

    conn.close()
    logging.info(f"Data for {url} appended to DuckDB.")

def analyze_domain(domain):
    logging.info(f"Analyzing {domain}")
    mobile_data = get_pagespeed_insights(domain, "mobile")
    mobile_filename = f"pagespeed_mobile_{domain.replace('https://', '').replace('http://', '').replace('/', '_')}.json"
    save_to_json(mobile_data, mobile_filename)  

    if "error" not in mobile_data: 
        append_to_duckdb(mobile_data, domain)

if __name__ == "__main__":
    con = duckdb.connect('/Users/tis/foam/github/seo_audit_reports/sources/seo/crawl.duckdb')
    domains = con.execute("""--sql
        SELECT DISTINCT domain 
        FROM prospect_emails
    """).fetchnumpy()['domain'].tolist()
    #domains = ['domain.com']

    # Check if there are any new domains to crawl
    existing_domains = con.execute("""--sql
        SELECT DISTINCT url 
        FROM pagespeed_mobile
    """).fetchnumpy()['url'].tolist()

    new_domains = set(domains) - set(existing_domains)

    con.close()

    if not new_domains:
        logging.info("No new domains to analyze. Exiting.")
        exit()

    total_domains = len(new_domains)
    logging.info(f"Found {total_domains} new domains to analyze.")

    # Set the number of threads
    num_threads = 12  

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(analyze_domain, new_domains)

    logging.info("Analysis complete.")