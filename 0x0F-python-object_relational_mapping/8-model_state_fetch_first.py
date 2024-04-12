#!/usr/bin/python3
"""
Starts a session with the database and queries the first state from
the states table.If no state is found, it prints "Nothing"
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
    state = session.query(State).first()
    if not state:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()
