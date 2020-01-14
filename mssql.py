import pyodbc
import logging
import sys

def db_connect(sqlserver, database):
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                            f'Server={sqlserver};'
                            f'Database={database};'
                            'Trusted_Connection=yes;'
                            )

        cursor = conn.cursor()
    except Exception as e:
        logging.error(msg='An error has occurred while connecting to your SQL server...')
        print(e)

    try:
        query = input("Please enter a query to run: ")
        cursor.execute(query)
        
    except Exception as e:
        logging.error(msg='An error has occurred running a query on your database...')
        print(e)

    for t in cursor:
        if t is None:
            logging.error(msg='Query returned no data...')
        else:
            print(t)

sqlserver = sys.argv[1]
database = sys.argv[2]

db_connect(sqlserver, database)
