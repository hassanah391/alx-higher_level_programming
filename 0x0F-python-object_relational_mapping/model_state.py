#!/usr/bin/python3
"""
Module that contains the class definition of a State and an instance Base.

State class:
- Inherits from Base
- Links to the MySQL table 'states'
- Has the following class attributes:
  - id: an auto-generated, unique integer, can't be null and is a primary key
  - name: a string with a maximum of 128 characters and can't be null

Usage:
- Connects to a MySQL server running on localhost at port 3306
- Creates the 'states' table in the specified database

Example:
    ./model_state.py <mysql username> <mysql password> <database name>
"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from Base
    - Links to the MySQL table 'states'
    - Has the following class attributes:
      - id: an auto-generated, can't be null and is a primary key
      - name: a string with a maximum of 128 characters and can't be null
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")


if __name__ == "__main__":
    import sys
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
