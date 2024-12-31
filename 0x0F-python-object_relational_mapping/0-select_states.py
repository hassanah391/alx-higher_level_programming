#!/usr/bin/python3
"""
Module 0-select_states
=======================
This module connects to a MySQL database and retrieves
all rows from the 'states' table.

Usage:
------
    $ ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Functions:
----------
- main(): Connects to the MySQL database, retrieves all rows
          from the 'states' table, and prints each row.

Example:
--------
    $ ./0-select_states.py root root_password hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
