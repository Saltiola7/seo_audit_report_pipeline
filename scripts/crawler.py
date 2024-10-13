import os
import time
import duckdb
import polars as pl
from datetime import datetime, timedelta

def crawl_website(sf_path, domain, output_folder):
    """
    Crawl the website using Screaming Frog CLI.
    """
    os.system(f"{sf_path} --crawl {domain} --project-name {domain} --headless --output-folder {output_folder} --export-format csv --export-tabs \"Internal:HTML\" --overwrite")
    time.sleep(15)

def read_csv_to_dataframe(csv_file):
    """
    Read the CSV file into a Polars DataFrame with specified columns.
    """
    columns = [
        "Address", "Word Count", "Indexability Status", "Title 1 Length", "Title 1",
        "Meta Description 1 Length", "Meta Description 1", "Meta Keywords 1",
        "Meta Keywords 1 Length", "H1-1", "H1-1 Length", "H1-2", "H1-2 Length",
        "H2-1", "H2-1 Length", "H2-2", "H2-2 Length", "Meta Robots 1",
        "X-Robots-Tag 1", "Meta Refresh 1", "Canonical Link Element 1", "Size (bytes)",
        "Transferred (bytes)", "Total Transferred (bytes)", "Sentence Count",
        "Average Words Per Sentence", "Flesch Reading Ease Score", "Readability",
        "Text Ratio", "Crawl Depth", "Folder Depth", "Link Score", "Inlinks",
        "Unique Inlinks", "Unique JS Inlinks", "% of Total", "Outlinks",
        "Unique Outlinks", "Unique JS Outlinks", "External Outlinks",
        "Unique External Outlinks", "Unique External JS Outlinks",
        "Closest Similarity Match", "No. Near Duplicates", "Spelling Errors",
        "Grammar Errors", "Hash", "Response Time", "Last Modified", "Redirect URL",
        "Redirect Type", "Cookies", "Language", "Mobile Alternate Link",
        "URL Encoded Address", "Crawl Timestamp",
        "Status", "Status Code", "Indexability"
    ]
    df = pl.read_csv(csv_file)

    # Filter columns based on availability in the CSV
    available_columns = [col for col in columns if col in df.columns]
    df = df.select(available_columns)

    # Add missing columns with null values
    for col in columns:
        if col not in df.columns:
            df = df.with_columns(pl.lit(None).alias(col))

    return df.with_columns([pl.col(col).cast(pl.Utf8) for col in df.columns])

def insert_data_to_duckdb(con, df):
    """
    Insert data from the DataFrame into the DuckDB table,
    handling cases where some columns might be missing and have spaces or hyphens,
    and mapping CSV header names to database column names.
    """
    con.register('df_view', df)

    # Define the mapping from CSV header names to database column names
    column_mapping = {
        "Address": "address",
        "Word Count": "word_count",
        "Indexability Status": "indexability_status",
        "Title 1 Length": "title_1_length",
        "Title 1": "title_1",
        "Meta Description 1 Length": "meta_description_1_length",
        "Meta Description 1": "meta_description_1",
        "Meta Keywords 1": "meta_keywords_1",
        "Meta Keywords 1 Length": "meta_keywords_1_length",
        "H1-1": "h1_1",
        "H1-1 Length": "h1_1_length",
        "H1-2": "h1_2",
        "H1-2 Length": "h1_2_length",
        "H2-1": "h2_1",
        "H2-1 Length": "h2_1_length",
        "H2-2": "h2_2",
        "H2-2 Length": "h2_2_length",
        "Meta Robots 1": "meta_robots_1",
        "X-Robots-Tag 1": "x_robots_tag_1",
        "Meta Refresh 1": "meta_refresh_1",
        "Canonical Link Element 1": "canonical_link_element_1",
        "Size (bytes)": "size_bytes",
        "Transferred (bytes)": "transferred_bytes",
        "Total Transferred (bytes)": "total_transferred_bytes",
        "Sentence Count": "sentence_count",
        "Average Words Per Sentence": "average_words_per_sentence",
        "Flesch Reading Ease Score": "flesch_reading_ease_score",
        "Readability": "readability",
        "Text Ratio": "text_ratio",
        "Crawl Depth": "crawl_depth",
        "Folder Depth": "folder_depth",
        "Link Score": "link_score",
        "Inlinks": "inlinks",
        "Unique Inlinks": "unique_inlinks",
        "Unique JS Inlinks": "unique_js_inlinks",
        "% of Total": "percentage_of_total",
        "Outlinks": "outlinks",
        "Unique Outlinks": "unique_outlinks",
        "Unique JS Outlinks": "unique_js_outlinks",
        "External Outlinks": "external_outlinks",
        "Unique External Outlinks": "unique_external_outlinks",
        "Unique External JS Outlinks": "unique_external_js_outlinks",
        "Closest Similarity Match": "closest_similarity_match",
        "No. Near Duplicates": "near_duplicates",
        "Spelling Errors": "spelling_errors",
        "Grammar Errors": "grammar_errors",
        "Hash": "hash",
        "Response Time": "response_time",
        "Last Modified": "last_modified",
        "Redirect URL": "redirect_url",
        "Redirect Type": "redirect_type",
        "Cookies": "cookies",
        "Language": "language",
        "Mobile Alternate Link": "mobile_alternate_link",
        "URL Encoded Address": "url_encoded_address",
        "Crawl Timestamp": "crawl_timestamp",
        "Status": "status",
        "Status Code": "status_code",
        "Indexability": "indexability"
    }

    # Construct the column list for the INSERT statement using the mapping
    columns_str = ', '.join([column_mapping.get(col, col) for col in df.columns])

    # Construct the SELECT statement dynamically, handling spaces and hyphens
    select_str = ', '.join([f'"{col}"' for col in df.columns])

    # Build the complete INSERT statement
    sql = f"""
        INSERT INTO internal_html ({columns_str})
        SELECT {select_str}
        FROM df_view
    """

    con.execute(sql)

def get_domains_after_date(con, cutoff_date):
    """
    Get domains from the database that have a timestamp after the specified cutoff date.
    """
    query = f"""
        SELECT DISTINCT domain 
        FROM prospect_emails 
        WHERE timestamp IS NOT NULL
        AND timestamp > '{cutoff_date}'
    """
    domains = con.execute(query).fetchnumpy()['domain'].tolist()
    return domains

def get_existing_domains(con):
    """
    Get domains that are already present in the internal_html table.
    """
    query = """
        SELECT DISTINCT regexp_extract(address, '://([^/]+)', 1) AS domain
        FROM internal_html
        WHERE address IS NOT NULL
    """
    result = con.execute(query).fetchall()
    existing_domains = [row[0] for row in result if row[0] is not None]
    return set(existing_domains)

def main():
    # Define constants
    sf_path = '/Applications/Screaming\ Frog\ SEO\ Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher'
    output_folder = '/Users/tis/github/seo_audit_reports/scripts/temp'
    db_file = '/Users/tis/github/seo_audit_reports/sources/seo/crawl.duckdb'
    csv_file = '/Users/tis/github/seo_audit_reports/scripts/temp/internal_html.csv'

    # Set the cutoff date (adjust this to your desired date)
    cutoff_date = datetime(2024, 9, 1)  # Example: September 1, 2024

    # Connect to the database
    con = duckdb.connect(db_file)

    # Get domains from the database after the cutoff date
    #domains = get_domains_after_date(con, cutoff_date)
    domains = ['moreliving.com.au']
    
    # Get existing domains from the internal_html table
    existing_domains = get_existing_domains(con)

    # Close the database connection
    con.close()

    # Filter out domains that are already in the internal_html table
    new_domains = [domain for domain in domains if domain.split('@')[-1] not in existing_domains]

    print(f"Total domains found: {len(domains)}")
    print(f"Domains already crawled: {len(domains) - len(new_domains)}")
    print(f"New domains to crawl: {len(new_domains)}")

    for domain in new_domains:
        print(f"Starting crawl for {domain}")

        # Extract the actual domain from the email address
        domain_to_crawl = domain.split('@')[-1]

        # Crawl the website
        crawl_website(sf_path, domain_to_crawl, output_folder)

        # Process and upload data
        try:
            con = duckdb.connect(db_file)
            df = read_csv_to_dataframe(csv_file)
            insert_data_to_duckdb(con, df)
            print(f"Data from {domain_to_crawl} appended to internal_html table successfully!")
        except Exception as e:
            print(f"An error occurred while processing {domain_to_crawl}: {e}")
        finally:
            con.close()

        print(f"Finished processing {domain_to_crawl}")
        time.sleep(5)  # Wait for 5 seconds before starting the next domain

    print("All new domains have been crawled and processed.")

if __name__ == "__main__":
    main()