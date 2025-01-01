#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and retrieves the
State object with the name passed as an argument. If the state is found,
it prints the state's id. Otherwise, it prints "Not found".

Usage:
    ./10-model_state_my_get.py <mysql_username>
            <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username: The username to connect to the MySQL database.
    mysql_password: The password to connect to the MySQL database.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for in the database.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    searched_name = sys.argv[4]
    # Create a connection to MySQL server on local host at port 3306
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #  prints the State object with the name passed as argument
    first_row = session.query(State.id).filter(State.name == searched_name) \
        .order_by(State.id).first()
    if first_row:
        print("{}".format(first_row.id))
    else:
        print("Not found")

    # Close the session and the engine
    session.close()
    engine.dispose()
