#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
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
    
    # Get the state name from arguments
    state_name = sys.argv[4]
    
    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()
    
    # Display the state id or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close the session
    session.close()
