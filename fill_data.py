from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

SCOPES = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "Alzheimer-ad3ecd64cce8.json"
SPREADSHEET = "Machine_learning_result"

credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPES)

"""
Writes the class probabilities to a remote spreadsheet
@param results: list of list of probabilities between <0, 1>, sorted from class 0 to 3
@param timestamps: list of timestamps for the probablility reports
"""


def write_results(results, timestamps):
    gc = gspread.authorize(credentials)

    workbook = gc.open(SPREADSHEET)
    sheet = workbook.sheet1

    # sheet.update_acell('A4', timestamps[0])
    # sheet.update_acell('B4', results[0][0])
    # sheet.update_acell('C4', results[0][1])
    # sheet.update_acell('D4', results[0][2])
    # sheet.update_acell('E4', results[0][3])

    for x in range(len(results)):
        row = 3 + len(results) - x
        print(row)
        sheet.update_acell('A' + str(row), timestamps[x])
        sheet.update_acell('B' + str(row), str(results[x][0]).replace('.', ','))
        sheet.update_acell('C' + str(row), str(results[x][1]).replace('.', ','))
        sheet.update_acell('D' + str(row), str(results[x][2]).replace('.', ','))
        sheet.update_acell('E' + str(row), str(results[x][3]).replace('.', ','))

    row = 4 + len(results)
    sheet.update_acell('B3', "=AVERAGE(B4:B" + str(row) + ")")
    sheet.update_acell('C3', "=AVERAGE(C4:C" + str(row) + ")")
    sheet.update_acell('D3', "=AVERAGE(D4:D" + str(row) + ")")
    sheet.update_acell('E3', "=AVERAGE(E4:E" + str(row) + ")")
