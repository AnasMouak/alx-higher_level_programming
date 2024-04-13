#!/usr/bin/python3
"""
Starts a session with the database and queries states from the states table.
It prints the ID of the first state whose name contains the specified string.
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    name_state = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).all()

    for state in states:
        if name_state == state.name:
            print(state.id)
            break

    else:
        print("Not found")

    session.close()
