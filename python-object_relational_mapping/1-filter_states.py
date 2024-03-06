#!/usr/bin/python3
"""
A script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

def filter_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states starting with 'N' sorted by id.
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    
    # Create a cursor object
    cur = db.cursor()
    
    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all the rows
    query_rows = cur.fetchall()
    
    # Print each row
    for row in query_rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
