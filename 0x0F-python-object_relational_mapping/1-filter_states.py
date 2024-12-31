#!/usr/bin/python3
"""
Module 1-filter_states
Lists all states with a name starting with N (upper N) from the database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    # Fetch all matching rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
