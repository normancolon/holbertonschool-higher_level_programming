#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assuming model_state.py is correctly set up
import sys

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine that connects to the specified database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects, ordered by their id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each State object
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
