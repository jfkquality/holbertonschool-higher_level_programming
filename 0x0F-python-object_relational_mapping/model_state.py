#!/usr/bin/python3
""" Base Class
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# """ Import sqlalchemy module """

Base = declarative_base()
# """ Base module """
# connect to server
# engine = create_engine('mysql://root:jknight121@localhost:3306')
# Base.metadata.create_all(engine)


class State(Base):
    """State subclass of Base"""
    # __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    # id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
