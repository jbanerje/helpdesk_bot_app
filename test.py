import pandas as pd

invalid_rec_df = pd.Series({
                "Ticket_Number": "Invalid Ticket.Try with valid ticket Number",
                "Description": "N/A",
                "Status": "N/A",
                "Completion": "N/A",
                "Assigned_To": "N/A"
                })

response_dict = invalid_rec_df.to_dict()

print(response_dict)