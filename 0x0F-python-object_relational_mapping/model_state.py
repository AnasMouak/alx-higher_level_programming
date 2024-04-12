#!/usr/bin/python3
"""contains the class definition of a State and an instance
    Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the states table in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
