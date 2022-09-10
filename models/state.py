#!/usr/bin/python3
""" Defines the state class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """
    Represents class State.

    Attributes:
        name (str): The name of the state object.
        __tablename__ (str): The name of the MySQL table.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            " Get a list of all related City objects."
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
                    
            return city_list