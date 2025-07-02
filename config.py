#importing libraries here
import os
from dotenv import load_dotenv

#loding
load_dotenv()

#set keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")