#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://root:@localhost:3306/mydatabase')
Base.metadata.create_all(engine)
