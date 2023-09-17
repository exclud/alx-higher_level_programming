#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_a(username, password, db_name):
    """
    Function to fetch all states containing 'a' from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    """
    Main function to prevent execution when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states_with_a(username, password, db_name)
