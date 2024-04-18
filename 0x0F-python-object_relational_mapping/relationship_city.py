#!/usr/bin/python3
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Represents the cities table in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the city.
        state_id (int): foreign key to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
