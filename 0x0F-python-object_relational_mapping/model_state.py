#!/usr/bin/python3
""" Base Class
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State subclass of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    # id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
