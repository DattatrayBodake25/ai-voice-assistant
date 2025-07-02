#importing libraries
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from config import GOOGLE_SHEET_ID


# Path to the credentials file
CREDS_PATH = "credentials.json"


# Define required scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


#writing function for google sheet 
def log_to_sheet(user_input: str, bot_response: str):
    try:
        # Authenticating and create a client
        creds = Credentials.from_service_account_file(CREDS_PATH, scopes=SCOPES)
        client = gspread.authorize(creds)

        # Opening the Google Sheet by its ID
        sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

        # Creating timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Appending new row
        sheet.append_row([timestamp, user_input, bot_response])
        print("Successfully logged to Google Sheet.")

    except Exception as e:
        print(f"Failed to log to sheet: {e}")