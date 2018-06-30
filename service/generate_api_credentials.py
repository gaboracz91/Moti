from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('../client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

spreadsheet_service = build('sheets', 'v4', http=creds.authorize(Http()))
