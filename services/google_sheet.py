import gspread

from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(credentials)


def get_sheet_data(sheet_url: str):
    sheet = client.open_by_url(sheet_url).sheet1
    print(f"Retrieved data from Google Sheet: {sheet.title}")
    return sheet.get_all_records()


# TEST
# sheet_url = "https://docs.google.com/spreadsheets/d/1rQvWqFS5ne40LluFPNMpuh3iy7DGtoKPwN9NOSFtSfA/edit?usp=sharing"

# data = get_sheet_data(sheet_url)

# print(data)