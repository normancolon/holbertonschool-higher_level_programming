#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
import sys

def filter_states_by_user_input(username, password, db_name, state_searched):
    """
    Connects to a MySQL database and lists all states where name matches
    the user-provided state name, sorted by id.
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
    
    # WARNING: This is not safe from SQL injection.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_searched)
    
    # Execute the SQL query
    cur.execute(query)
    
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
        filter_states_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
