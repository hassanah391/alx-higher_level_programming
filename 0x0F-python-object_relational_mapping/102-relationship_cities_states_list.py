#!/usr/bin/python3
"""
This script lists all City objects from the database specified by the user,
along with their corresponding State names.
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
