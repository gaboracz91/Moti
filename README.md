# ImOkCore
Welcome to ImOkCore documentation. This is a small django project with a rest API, and a management command to write google sheets. It is deployed using Heroku, and the scheduling is handled by Zapier.
The address of the web service is: www.imokcore.heroku.com

## How to use
The two main functionality of the service is to allow the admin to log in, add new members to the program, who will have to log into the site on a daily base(Monday to Friday) and click the central button, otherwise they will be present on the next day's google sheet.

### For Users
As a member of the program follow these steps:
* Step 0: Have the admin add you to the program as a member, giving your name, username, password, email address and phone number.
* Step 1: Go to www.imokcore.heroku.com
* Step 2: Log in using the username and password set together with you admin
* Step 3: Press the button in the center of the screen
* Step 4: Log out using the "logout" button at the top right corner of the website
* Step 5: Feel accomplished

### For Admins
As an admin, your main use of the site is to add or remove members from the program. Remember to only delete a member if you have clear, written confirmation from the project lead. Also remember, in order to add new member, you need the following information: name, username, password, email address and phone number.
* Step 0: Have the developer add you as an admin
* Step 1: Go to www.imokcore.heroku.com/admin
* Step 2: Log in using the username and password set by your developer
* Step 3a: To add a new member, select "Add" in the row with "Users"
* Step 4a: Fill out all fields, then click "Save" in the button right corner, or "Save and add another" if you would like to add multiple members

* Step 3b: To remove an existing member, select "Change" in the row with "Users"
* Step 4b: Find the member using the table or the search function
* Step 5b: Select the member/s by clicking the checkbox on the left side of the row
* Step 6b: Next to the "Action", click the "-------" drop down, and select "delete selected user"
* Step 7b: Click to "Go" button to delete the member/s
* Step 8b: *Find a new member*

## Deployment

* git push heroku master
* heroku ps:clock scale=1