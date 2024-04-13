#!/usr/bin/python3
"""
Starts a session with the database and change a state
It Change the name of the State where id = 2 to New Mexico
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
        if state.id == 2:
            state.name = "New Mexico"
            session.commit()
    session.close()
