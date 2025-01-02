#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
in the database specified by the user.
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
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
    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)
    session.add(new_s)
    session.add(new_c)
    session.commit()
    session.close()
