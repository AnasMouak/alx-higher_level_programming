#!/usr/bin/python3
"""
Starts a session with the database and print all City objects from the database
hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    mix = session.query(State.name, City.id, City.name).join(City).all()
    for mixed in mix:
        print(f"{mixed[0]}: ({mixed[1]}) {mixed[2]}")

    session.close()
