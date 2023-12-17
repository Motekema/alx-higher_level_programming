#!/usr/bin/python3
"""Defines the State class and sets up the Bas"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents the state for a MySQL database.

    __tablename__ (str): the name of the MySQL table to store States.
    id (sqlalchemy.Integer): A state's id.
    name (sqlalchemy.String): A state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
