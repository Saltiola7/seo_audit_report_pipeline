import advertools as adv
import pandas as pd

sitemap_index = adv.sitemap_to_df("https://www.imagegroup.com.au/sitemap_index.xml", recursive=False)
sitemap_urls = sitemap_index['loc']

all_sitemaps = []
for url in sitemap_urls:
    all_sitemaps.append(adv.sitemap_to_df(url))

all_links = pd.concat(all_sitemaps)

# Select only the 'loc' column
all_links_loc = all_links['loc']

# Crawl the URLs, ignoring robots.txt, and saving to a jsonlines file
adv.crawl(
    all_links_loc.tolist(),  # Convert the Series to a list
    'scripts/temp/advertools.jsonl',       # Output file path
    follow_links=False,      # Crawl only the provided URLs
    custom_settings={        # Custom settings for the crawler
        "ROBOTSTXT_OBEY": False  # Ignore robots.txt
    }
)

# Read the crawled data
crawled_data = pd.read_json('scripts/temp.jl', lines=True)

# Print the crawled data (optional)
print(crawled_data)
