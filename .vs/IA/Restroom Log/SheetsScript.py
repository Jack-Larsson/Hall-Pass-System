from time import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials


gc = gspread.oauth(
    credentials_filename=r'D:\s1649121\Documents\VS Projects\PublicEnemy1\.vs\IA\Restroom Log\googlecreds.json'
)
gsheet = gc.open_by_key("1oMakpyyRqNZyMroZ-P6pcBn3dmfjeccDAPllFPeg9xc")
wsheet = gsheet.worksheet("Sheet1")
mydata = wsheet.get_all_records()

t = localtime()
current_time = strftime("%H:%M:%S", t)

def printstudent(last, first):
    wsheet.append_row([last, first, current_time])