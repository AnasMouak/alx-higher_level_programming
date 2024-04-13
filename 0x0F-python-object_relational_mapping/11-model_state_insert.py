#!/usr/bin/python3
"""
Starts a session with the database and adds a new state to the states table.
It prints the ID of the newly added state.
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
