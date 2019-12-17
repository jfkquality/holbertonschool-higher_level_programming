#!/usr/bin/python3
""" Base Class
"""
import SQLAlchemy
from SQLAlchemy import create_engine
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy import Column, Integer, String

Base = declarative_base()

# connect to server
engine = create_engine('mysql://root:jknight121@localhost:3306')
Base.metadata.create_all(engine)


class State(Base):
    """State subclass of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

# Duplicate for cities
