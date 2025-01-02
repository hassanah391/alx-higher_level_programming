#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy, adds a new State
object with the name 'Louisiana' to the 'states' table, and prints the id of
the newly added State.
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

    # Add a new row
    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    # Print the id of the last row that I've added
    last_row = session.query(State.id).filter(State.name == "Louisiana") \
        .order_by(State.id).first()
    print("{}".format(last_row.id))

    # Close the session and the engine
    session.close()
    engine.dispose()
