#!/usr/bin/python3
"""
Starts a session with the database and delet a state
It delet the name of the State where a name containing the letter a
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
            session.delete(state)
            session.commit()

    session.close()
