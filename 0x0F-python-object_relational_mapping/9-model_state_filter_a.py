#!/usr/bin/python3
"""
This module lists all State objects from the database that contain the letter
'a' in their name.

Usage:
  ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The name of the database to connect to.

Example:
    ./9-model_state_filter_a.py root root_password hbtn_0e_6_usa

This script connects to a MySQL server running on localhost at port 3306 using
the provided MySQL username, password, and database name. It then queries the
'states' table for all State objects that contain the letter 'a' in their name,
ordered by their IDs, and prints each state's ID and name.

The script uses SQLAlchemy to handle database interactions and ORM
(Object-Relational Mapping).
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    # Create a connection to MySQL server on local host at port 3306
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # lists all State objects that contain the letter 'a'
    for id, name in session.query(State.id, State.name) \
            .filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(id, name))

    # Close the session and the engine
    session.close()
    engine.dispose()
