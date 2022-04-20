# DB connection

import mysql.connector

host = "comp4442-group-project.coa9uj3ys1py.us-east-1.rds.amazonaws.com"
user = "admin"
password = "12345678"
port = 3306
database = "comp4442-group-project"

def connection():
    # connect to database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
        port=port
    )

    return conn