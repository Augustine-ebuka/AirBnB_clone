#!/usr/bin/python3
"""Define the review object"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the Review class

    Attributes:
        price_id(str): the price of the place
        user_id(str): The user id of the user
        text(str): The text of the review
    """

    place_id = ""
    user_id = ""
