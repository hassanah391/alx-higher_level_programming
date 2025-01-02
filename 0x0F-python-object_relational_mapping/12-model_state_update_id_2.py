#!/usr/bin/python3
"""
This script updates the name of a State object with id = 2 to "New Mexico"
in a MySQL database using SQLAlchemy ORM. It then lists all State objects
from the database.

Usage: ./12-model_state_update_id_2.py
            <mysql_username> <mysql_password> <database_name>
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

    # Update the name of a State object that has id = 2
    state = session.query(State).where(State.id == 2).one()
    state.name = "New Mexico"
    session.add(state)
    session.commit()

    # lists all State objects
    for id, name in session.query(State.id, State.name) \
            .order_by(State.id).all():
        print("{}: {}".format(id, name))

    # Close the session and the engine
    session.close()
    engine.dispose()
