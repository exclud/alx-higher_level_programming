#!/usr/bin/python3
"""
Module for changing the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, db_name):
    """
    Function to change the name of a State object from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    change_state_name(username, password, db_name)
