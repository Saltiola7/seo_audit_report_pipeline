import json
import re
import csv

def extract_content_fields(jl_file, output_file):
    """
    Extracts content fields (title, meta_desc, h1, body_text) from a JSON Lines file, 
    cleans the body_text, and saves the output to a CSV file.

    Args:
        jl_file (str): Path to the input JSON Lines file.
        output_file (str): Path to the output CSV file.
    """

    data = []

    with open(jl_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                page_data = json.loads(line)
                content = {
                    'title': page_data.get('title'),
                    'meta_desc': page_data.get('meta_desc'),
                    'h1': page_data.get('h1'),
                    'body_text': page_data.get('body_text').strip()
                }

                # Remove phone number patterns at the beginning using regex
                content['body_text'] = re.sub(r"^\s*CALL NOW.*?\n\s*\n", "", content['body_text'])

                # Remove all newline characters from body_text
                content['body_text'] = content['body_text'].replace('\n', '')

                data.append(content)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Write the extracted data to a CSV file
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['title', 'meta_desc', 'h1', 'body_text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

# Example usage:
jl_filepath = 'scripts/temp/advertools.jsonl'
output_filepath = 'scripts/temp/parsed_advertools.csv'
extract_content_fields(jl_filepath, output_filepath)