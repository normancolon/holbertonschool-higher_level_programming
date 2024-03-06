#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Ensure model_state.py is correctly set up
import sys

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine that connects to the specified database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects with a name containing 'a' and delete them
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to the database to save the changes
    session.commit()

    # Close the session
    session.close()
