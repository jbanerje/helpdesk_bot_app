# helpdesk_bot_app

This app is a simple backend API for helpdesk chatbot

create_db.py - This code will create database helpdesk_request.db thru sqlite

flask_app.py - Flask API to receive post from chatbotw with tcket number and responding the status of the ticket.

Request Type : POST

Header
    Content-Type : application/json

Sample body :
[
    {
        "Ticket_Num": 11111
    }
]

Sample Output:
{
    "Ticket_Number": 11111,
    "Description": "Software Request - Install Python",
    "Status": "In Progress",
    "Completion": "12/26/2020",
    "Assigned_To": "John Doe"
}

