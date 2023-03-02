from datetime import date
from schedule import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(
    filename= r"/home/hanskonstantin/PublicEnemy1/.vs/IA/Restroom Log/hall-pass-creds.json" )  
gsheet = gc.open_by_key("1oMakpyyRqNZyMroZ-P6pcBn3dmfjeccDAPllFPeg9xc")

todaysdate = date.today()
today = todaysdate.strftime('%m/%d/%Y')
print(today)

#create worksheet with todays date as the title
def MakeToday():
    worksheet = gsheet.add_worksheet(title= today, rows=100, cols=5)
    return worksheet

#open new worksheet as wsheet, if it doesn't exist yet create new sheet
#finally return wsheet so that it can be accessed in other methods
def OpenToday():
    wsheet = ""
    try:
        wsheet = gsheet.worksheet(today)
    except gspread.exceptions.WorksheetNotFound:
        MakeToday()
        OpenToday()
    finally:
        return wsheet

#schedule creation of new worksheet for midnight everyday
every().day.at("00:00:00").do(MakeToday)
#open wsheet after creating
OpenToday()


#write student name, the time they left, and the time they returned to spreadsheet
def printstudent(last, first, timein, timeout):
    OpenToday().append_row([last, first, timein, timeout])