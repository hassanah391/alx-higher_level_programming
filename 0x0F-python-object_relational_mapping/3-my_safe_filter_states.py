#!/usr/bin/python3
"""
Module 3-my_safe_filter_states
Lists all states from the database hbtn_0e_0_usa
where name matches the argument.
safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":
    searchedName = sys.argv[4]
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("\
                SELECT * \
                FROM states \
                WHERE name = '{}'\
                ORDER BY id ASC;\
                ".format(searchedName.replace("'", "''")))

    # Fetch all matching rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
