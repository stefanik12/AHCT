from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

SCOPES = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "Alzheimer-ad3ecd64cce8.json"
SPREADSHEET = "Machine_learning_result"


credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPES)
gc = gspread.authorize(credentials)

workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1

all_cells = sheet.range('A1:C6')
print(all_cells)

sheet.update_acell('B4', '50%')
sheet.update_acell('D4', '10%')

