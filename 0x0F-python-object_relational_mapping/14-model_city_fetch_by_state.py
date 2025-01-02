#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py
        <mysql username> <mysql password> <database name>
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connet to the databse
    user = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for q in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(q[0], q[1], q[2]))

    session.close()
