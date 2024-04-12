#!/usr/bin/python3
"""
Starts a session with the database and queries states from the states table.
It prints the ID and name of states where the name contains the letter 'a'.
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).all()
    for state in states:
        if "a" in state.name:
            print(f"{state.id}: {state.name}")

    session.close()
