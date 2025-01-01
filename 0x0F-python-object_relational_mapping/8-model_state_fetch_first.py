#!/usr/bin/python3
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

    # Fetch first row in states table ordered by id
    first_row = session.query(State).order_by(State.id).first()
    if first_row:
        print("{}: {}".format(first_row.id, first_row.name))
    else:
        print("Nothing")

    # Close the session and the engine
    session.close()
    engine.dispose()
