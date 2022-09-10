#!/usr/bin/python3
""" Defines  city class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    Represents class.

    Attributes:
        state_id (str): The id of the state.
        name (str): The name of the state.
        __tablename__ (str): The name of the MySQL table.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
