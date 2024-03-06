#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

def list_cities(username, password, db_name):
    """
    Connects to a MySQL database and lists all cities sorted by city ids
    along with their state names.
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
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """)
    
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
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
