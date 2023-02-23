from time import *
from datetime import date
from schedule import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

t = localtime()
today = date.today()
today.strftime('%m/%d/%Y')
current_time = strftime("%H:%M:%S", t)

gc = gspread.oauth(
    credentials_filename=r'D:\s1649121\Documents\VS Projects\PublicEnemy1\.vs\IA\Restroom Log\googlecreds.json'
)

gsheet = gc.open_by_key("1oMakpyyRqNZyMroZ-P6pcBn3dmfjeccDAPllFPeg9xc")

def TodaysSheet():
    worksheet = gsheet.add_worksheet(title= today, rows=100, cols=5)

every().day.at("8:30").do(TodaysSheet())
wsheet = gsheet.worksheet(today)

#write student name, the time they left, and the time they returned to spreadsheet
def printstudent(last, first):
    wsheet.append_row([last, first, current_time])