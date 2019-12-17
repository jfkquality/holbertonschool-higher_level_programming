#!/usr/bin/python3
""" Base Class
"""

# import SQLAlchemy
# from SQLAlchemy import create_engine
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy import Column, Integer, String
""" Import sqlalchemy module """

Base = declarative_base()
""" Base module """


class State(Base):
    """State subclass of Base"""
    __tablename__ = 'states'
    # id = Column(Integer, primary_key=True, nullable=False, unique=True)
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
