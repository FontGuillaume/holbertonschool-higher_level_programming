#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine and connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects containing letter 'a' and order by id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    
    # Display results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()
