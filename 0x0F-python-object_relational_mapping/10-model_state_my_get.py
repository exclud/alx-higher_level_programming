#!/usr/bin/python3
"""
Module for fetching a state by name from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_state_by_name(username, password, db_name, state_name):
    """
    Function to fetch a state by name from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    fetch_state_by_name(username, password, db_name, state_name)
