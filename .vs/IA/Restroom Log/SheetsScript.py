from time import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#create credentials to access and open spread sheet
gc = gspread.oauth(
    credentials_filename=r'C:\Users\s1649121\Documents\IA\.vs\IA\Restroom Log\googlecreds.json'
)
gsheet = gc.open_by_key("1oMakpyyRqNZyMroZ-P6pcBn3dmfjeccDAPllFPeg9xc")
wsheet = gsheet.worksheet("Sheet1")
mydata = wsheet.get_all_records()

#return time
t = localtime()
current_time = strftime("%H:%M:%S", t)

#write student name, the time they left, and the time they returned to spreadsheet
def printstudent(last, first):
    wsheet.append_row([last, first, current_time])