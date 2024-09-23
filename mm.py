import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import sys

#TODO: add all sheets from which you want to get data stream
ids = ["__",
       "__",
       "__",
       "__",
       "__",
       "__"]

day = int(sys.argv[1])

CRED_FILE = '/root/go/tg_bot/cred.json' #root/bgg/tg_bot/cred.json

sheet_id = ids[day-1]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CRED_FILE, 
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId= sheet_id,
    range='C2:C', #TODO: поменять колонны для данных
    majorDimension='COLUMNS'
).execute()

if 'values' in values:
    f = open(f'/root/go/tg_bot/tests/day{day}.txt', 'w', encoding='utf-8')
    for line in values['values']:
        for l in line:
            if l[len(l)-1] == " ":
                l = l[:len(l)-1]
            f.write(l + "\n")
    f.close()
