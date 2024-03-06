#!/usr/bin/python3
"""
A script that changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
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

    # Find the State object with id = 2
    state_to_update = session.query(State).get(2)

    # Check if the state exists, then update its name to 'New Mexico'
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
