from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

spreadsheet = build('sheets', 'v4', http=creds.authorize(Http())).spreadsheets()

body = {'properties': {'title': 'Call List'}}

request = spreadsheet.create(body=body)
response = request.execute()

print(response)

spreadsheet_id = response['spreadsheetId']

batch_update_values_request_body = {
    "valueInputOption": "RAW",

    # The new values to apply to the spreadsheet.
    'data': [
        {
            "values": [
                [
                    "Name",
                    "Age",
                    " Gender",
                    "Phone number",
                    "Called"
                ],
                [
                    1,
                    2,
                    3,
                    4,
                    '☑'
                ]
            ],
            "range": "Sheet1!A1:E2"
        }
    ],

    # TODO: Add desired entries to the request body.
}

request2 = spreadsheet.values().batchUpdate(spreadsheetId=spreadsheet_id,
                                            body=batch_update_values_request_body)
response2 = request2.execute()

print(response2)
