#!/usr/bin/python3
"""
Module for fetching all states from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_all_states(username, password, db_name):
    """
    Function to fetch all states from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    fetch_all_states(username, password, db_name)
