#!/usr/bin/python3
""" Defines Review class."""
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey, Column


class Review(BaseModel):
    """
    Represents Review class.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store reviews.
        place_id (str): The id of the Place object.
        user_id (str): The id of the User object.
        text (str): Text about review.
    """
    __tablename = "reviews"
    place_id = Column(String(60), ForeignKey("places_id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullale=False)
    text = Column(String(1024), nullable=False)
