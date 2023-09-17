#!/usr/bin/python3
"""Module for fetching the first state from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_first_state(username, password, db_name):
    """Fetches the first state from the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    """Main function to prevent execution when imported"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    fetch_first_state(username, password, db_name)
