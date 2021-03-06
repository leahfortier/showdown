import os.path
import pickle
from typing import List

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from main.util.constants import CREDENTIALS_FILE, PICKLE_FILE


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_credentials():
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is created
    # automatically when the authorization flow completes for the first time.
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_sheet_data(spreadsheet_id: str, range_name: str) -> List[List[str]]:
    service = build('sheets', 'v4', credentials=get_credentials())

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    service.close()
    return values
