#!/usr/bin/python3
"""
Module for adding a new state to the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, db_name):
    """
    Function to add a new state to the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("{}".format(new_state.id))

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    add_state(username, password, db_name)
