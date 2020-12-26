
#------------------------------------------------------------------------------------------------------------------------------#
# PROJECT    : Helpdesk API for kore.ai bot                                            
# DATE       : 12/24/2020                                                      
# WRITTEN BY : JAGANNATH BANERJEE                                
#-------------------------------------------------------------------------------------------------------------------------------#

# Import Libraries
from schema import Schema, And, Use, Optional, SchemaError
from flask import Flask, request, jsonify, Response
import pandas as pd
from create_db import FetchFromTable
import sqlite3
import json

app = Flask(__name__)

@app.route('/helpdesk-api', methods=['POST'])

def helpdesk_json():
    
    '''
    Input               : Input to this function is JSON string containing ticket#.
    Ouput               : Ouput to this function is JSON string containing ticket status.
    '''
    conn    = sqlite3.connect('helpdesk_request.db')
    schema = Schema([{'Ticket_Num': And(int)}])
    
    # Invalid record format
    invalid_rec_sr = pd.Series({
                                "Ticket_Number": "Invalid Ticket.Try with valid ticket number.",
                                "Description": "N/A",
                                "Status": "N/A",
                                "Completion": "N/A",
                                "Assigned_To": "N/A"
                                })

    # get the json string
    req_data = request.get_json()
        
    try:
        schema.validate(req_data)
        
        ticket_num = req_data[0]['Ticket_Num']

        # Fetch the request from database
        query = f'''SELECT * FROM helpdesk_req where Ticket_Number = {ticket_num}'''
        fetch_data_from_table = FetchFromTable(conn)
        qry_result = fetch_data_from_table.fetch_data(query)

        if qry_result.shape[0] > 0:

            # Create Response JSON
            response_dict = qry_result.to_dict(orient='records')
            response_dict = response_dict[0]
            resp = json.dumps(response_dict,ensure_ascii = False)
            
            response_json = Response(response     = resp, 
                                    status        = 200,
                                    content_type  = "application/json; charset=utf-8"
                                    )
        else:
            response_dict = invalid_rec_sr.to_dict()
            resp = json.dumps(response_dict,ensure_ascii = False)

            response_json = Response(response     = resp, 
                                    status        = 400,
                                    content_type  = "application/json; charset=utf-8")            

    except SchemaError as json_sch_err:
        response_json = response_json = str(json_sch_err)

    return response_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)