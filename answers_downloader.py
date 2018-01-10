from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

from answers_transform import transform_answers

SCOPES = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "Alzheimer-ad3ecd64cce8.json"
SPREADSHEET = "Questionnaire_answers"

credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPES)


def download_answer_sheet():
    gc = gspread.authorize(credentials)
    print("The following sheets are available")
    for sheet in gc.openall():
        print("{} - {}".format(sheet.title, sheet.id))

    workbook = gc.open(SPREADSHEET)
    # Get the first sheet
    sheet = workbook.sheet1

    return pd.DataFrame(sheet.get_all_records())

