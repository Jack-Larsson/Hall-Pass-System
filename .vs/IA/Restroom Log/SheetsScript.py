from time import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials


gc = gspread.service_account(filename='mycredentials.json')
gsheet = gc.open_by_key("1oMakpyyRqNZyMroZ-P6pcBn3dmfjeccDAPllFPeg9xc")
wsheet = gsheet.worksheet("Sheet1")
mydata = wsheet.get_all_records()

t = localtime()
current_time = strftime("%H:%M:%S", t)

def printstudent(last, first, timein,timeout):
    wsheet.inset_row(last, first, timein, timeout)