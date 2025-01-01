#!/usr/bin/python3
"""
Module 4-cities_by_state
Lists all cities from the database hbtn_0e_4_usa.
Shows all cities with their state relationships.

Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(""" SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id;
                """)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
