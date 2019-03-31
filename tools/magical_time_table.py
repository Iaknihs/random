import gspread
from oauth2client.service_account import ServiceAccountCredentials
from definitions import ROOT_DIR

"""
    WORK IN PROGRESS!
"""


def get_client(keyfile=ROOT_DIR+'\\assets\\private\\sheets_client_secret.json', scopes=None):
    """
    generate an authorized gspread client using a given keyfile.

    :param keyfile:
    :param scp:
    :return:
    """

    if scopes is None:
        # default scope, this should remain unchanged unless you know what you're doing.
        scopes = ['https://spreadsheets.google.com/feeds' + ' ' + 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(keyfile, scopes)
    client = gspread.authorize(creds)
    return client


def stuff(client):

    sheet = client.open("MagicalTimeTable").sheet1
    print("~~~")
    print(sheet.cell(1, 1).value)
    print("---")


if __name__ == '__main__':
    stuff(get_client())
