#!/usr/bin/python3
""" Defines class Place."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Place(BaseModel, Base):
    """
    Represents Place class.

    Attributes:
        city_id (str): The City object id.
        user_id (str): The user id.
        name (str): The name of the Place objet.
        description (str): Description about the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The number of maximum guest place can hold.
        price_by_night (int): The price of the night time.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): The id of the amenity object id.
    """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False)
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
