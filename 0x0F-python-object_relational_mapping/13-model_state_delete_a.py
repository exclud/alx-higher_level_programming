#!/usr/bin/python3
"""
Module for deleting all State objects with a name containing the letter a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# def delete_states_with_a(username, password, db_name):
#     """
#     Function to delete all State objects with a name containing the letter a
#     """
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
#                            .format(username, password, db_name), pool_pre_ping=True)
#     Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     for state in session.query(State).filter(State.name.contains('a')):
#         session.delete(state)
#     session.commit()

# if __name__ == "__main__":
#     """
#     Main function to prevent execution when imported
#     """
#     username = sys.argv[1]
#     password = sys.argv[2]
#     db_name = sys.argv[3]
#     delete_states_with_a(username, password, db_name)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()