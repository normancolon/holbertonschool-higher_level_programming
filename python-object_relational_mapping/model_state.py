#!/usr/bin/python3
"""
Definition of the State class and an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance of declarative_base
Base = declarative_base()

class State(Base):
    """
    State class:
    - inherits from Base
    - links to the MySQL table states
    - has an id and a name attribute
    """
    __tablename__ = 'states'  # Links to MySQL table states
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # Auto-generated, unique integer, can't be null, primary key
    name = Column(String(128), nullable=False)  # String with max 128 chars, can't be null
