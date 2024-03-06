#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State  # Import Base and State

if __name__ == "__main__":
    # Create an engine that connects to the specified database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create all tables in the engine (This is equivalent to "Create Table" statements in raw SQL)
    Base.metadata.create_all(engine)
