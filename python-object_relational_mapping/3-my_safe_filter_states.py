#!/usr/bin/python3
"""
A script that safely takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safe from MySQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
import sys

def safe_filter_states(username, password, db_name, state_name):
    """
    Connects to a MySQL database and lists all states matching the provided state name,
    safe from SQL injections.
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
    
    # Execute the SQL query safely
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    
    # Fetch all the rows
    query_rows = cur.fetchall()
    
    # Print each row
    for row in query_rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
