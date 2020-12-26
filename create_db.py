import sqlite3
import pandas as pd
import sys

class CreateTable:
    
    def __init__(self, cursr, table_name, table_defn):
        self.cursr          = cursr
        self.table_name     = table_name
        self.table_defn     = table_defn

    def create_table(self):
        try:
            self.cursr.execute(f'''CREATE TABLE {self.table_name} {tuple(self.table_defn)}''')
            print ('Table Created Sucessfully - {} '.format(self.table_name))
        except :
            print('Table Creation Failed - {}'.format(sys.exc_info()[0]))
        return

class InsertIntoTable:
    
    def __init__(self, conn, cursr, table_name):
        self.conn           = conn
        self.cursr          = cursr
        self.table_name     = table_name

    def insert_record(self, record):
        try:
            self.record = record
            self.cursr.execute(f'''INSERT INTO {self.table_name} VALUES {self.record}''')
            self.conn.commit()
            print ('Record Updated Sucessfully - {} '.format(self.record))
        except :
            print ('Record Update Failed - {}'.format(sys.exc_info()[0]))
        return

class FetchFromTable:
    
    def __init__(self, conn):
        self.conn = conn
    
    def fetch_data(self, query):
        self.query = query        
        query_result_df = pd.read_sql(query, self.conn)
        return query_result_df


if __name__ =="__main__":
    
    conn    = sqlite3.connect('helpdesk_request.db')    
    cursr   = conn.cursor()

    table_name = 'helpdesk_req'
    
    table_defn = {  'Ticket_Number' : 'real primary key', 
                    'Description'   : 'text',
                    'Status'        : 'text',
                    'Completion'    : 'text', 
                    'Assigned_To'   : 'text'
                }
    
    # Create Table
    create_table = CreateTable(cursr, table_name, table_defn)
    create_table.create_table()

    # # Update Records
    update_rec_into_table = InsertIntoTable(conn, cursr, table_name)
    update_rec_into_table.insert_record((11111, 'Software Request - Install Python','In Progress', '12/26/2020', 'John Doe'))
    update_rec_into_table.insert_record((22222, 'Ad Request - Linux Access','Complete', '12/25/2020', 'Mark Hussey'))
    update_rec_into_table.insert_record((33333, 'Hardware Request- Wireless Mouse','Started', '12/31/2020', 'Don Bradley'))

    
    #Fetch data
    query = f'''SELECT * FROM {table_name}'''
    fetch_data_from_table = FetchFromTable(conn)
    qry_result = fetch_data_from_table.fetch_data(query)
    print(qry_result)