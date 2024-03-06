#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa, safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
"""

import MySQLdb
import sys

def list_cities_by_state(username, password, db_name, state_name):
    """
    Connects to a MySQL database and lists all cities of a given state,
    sorted by cities.id.
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
    cur.execute("""
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """, (state_name,))
    
    # Fetch all the rows
    query_rows = cur.fetchall()
    
    # Extract city names and print them comma-separated
    cities = [row[0] for row in query_rows]
    print(", ".join(cities))
    
    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
