from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import re
import polars as pl
import duckdb

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def get_emails_with_label(service, label_id):
    """Gets a list of email IDs with the specified label."""
    results = service.users().messages().list(userId='me', labelIds=[label_id]).execute()
    messages = results.get('messages', [])
    email_ids = [message['id'] for message in messages]
    return email_ids

def get_label_id(service, label_name):
    """Gets the ID of a label by its name."""
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    return None

def get_email_address_and_name(service, email_id):
    """Gets the email address, full name, and received timestamp (as string) from a message."""
    message = service.users().messages().get(userId='me', id=email_id, format='full').execute()
    headers = message['payload']['headers']
    email_address = None
    full_name = None
    timestamp_str = None  # Store the raw timestamp string

    for header in headers:
        if header['name'] == 'From':
            from_header = header['value']
            match = re.search(r'<(.*?)>', from_header)  # Use regular expressions here
            if match:
                email_address = match.group(1)
            else:
                email_address = from_header.strip()

            # Extract full name (if available)
            full_name = from_header.split('<')[0].strip()
            if full_name.startswith('"') and full_name.endswith('"'):
                full_name = full_name[1:-1]

        if header['name'] == 'Date':
            timestamp_str = header['value']  # Store the raw date string

    return email_address, full_name, timestamp_str


if __name__ == '__main__':
    service = get_gmail_service()
    label_name = '1. Sales Pipeline/1. Prospects'
    label_id = get_label_id(service, label_name)
    db_file = '/Users/tis/foam/github/seo_audit_reports/sources/seo/crawl.duckdb'  # DuckDB database file

    if label_id:
        email_ids = get_emails_with_label(service, label_id)
        email_data = []

        for email_id in email_ids:
            email_address, full_name, timestamp_str = get_email_address_and_name(service, email_id)
            if email_address:
                domain = email_address.split('@')[-1]
                email_data.append({'email': email_address, 'full_name': full_name, 'domain': domain, 'timestamp': timestamp_str})

        # Create a Polars DataFrame
        df = pl.DataFrame(email_data)

        # Connect to DuckDB
        con = duckdb.connect(db_file)

        # Insert only new distinct emails (assuming the table already exists)
        con.execute("""--sql
            INSERT INTO prospect_emails 
            SELECT DISTINCT email, full_name, domain, timestamp 
            FROM df
            WHERE email NOT IN (SELECT email FROM prospect_emails)
        """)

        con.close()

        print("Data inserted into DuckDB table 'prospect_emails'.")

    else:
        print(f"Label '{label_name}' not found in your Gmail account.")