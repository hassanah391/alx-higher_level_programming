#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
