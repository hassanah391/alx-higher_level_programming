#!/usr/bin/python3
"""
This module fetches all rows in the states table of a MySQL database
and prints them ordered by id. The database connection details are
provided as command-line arguments.
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

    # Fetch all rows in states table ordered by id
    for id, name in session.query(State.id, State.name) \
            .order_by(State.id).all():
        print("{}: {}".format(id, name))

    # Close the session and the engine
    session.close()
    engine.dispose()
