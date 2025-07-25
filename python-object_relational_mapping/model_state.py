#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base
    
    Attributes:
        id (int): Unique identifier for each state
        name (str): Name of the state
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
