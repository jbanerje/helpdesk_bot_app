
#------------------------------------------------------------------------------------------------------------------------------#
# PROJECT    : Helpdesk API for kore.ai bot                                            
# DATE       : 12/24/2020                                                      
# WRITTEN BY : JAGANNATH BANERJEE                                
#-------------------------------------------------------------------------------------------------------------------------------#

# Import Libraries
from schema import Schema, And, Use, Optional, SchemaError
from flask import Flask, request, jsonify, Response
import pandas as pd
import datetime
import json
import os


app = Flask(__name__)

@app.route('/helpdesk-api', methods=['POST'])

def helpdesk_json():
    '''
    Input               : Input to this function is JSON string containing ticket#.
    Ouput               : Ouput to this function is JSON string containing ticket status.
    '''
    ticket_df = pd.DataFrame({'Ticket_Number':[12345, 67890],
                                'Status':['Assigned', 'Complete'],
                                'Completion':['12/31/2020', '12/25/2020'],
                                'Assigned_To':['Atul Kamble', 'Jagannath Banerjee']
                            })

    schema = Schema([{'Ticket_Num': And(int)}])
    
    # get the json string
    req_data = request.get_json()
        
    try:
        schema.validate(req_data)

        df = ticket_df[ticket_df.Ticket_Number == req_data[0]['Ticket_Num']]

        response_dict = df.to_dict(orient='records')
        
        resp = json.dumps(response_dict,ensure_ascii = False)
        
        response_json = Response(response     = resp, 
                                 status       = 200,
                                 content_type = "application/json; charset=utf-8"
                                )

    except SchemaError as json_sch_err:

        response_json = str(json_sch_err)

    return response_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)