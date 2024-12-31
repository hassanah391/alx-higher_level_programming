#!/usr/bin/python3
"""
Module 1-filter_states
Lists all states with a name starting with N (upper N) from the database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%';")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
