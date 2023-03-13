#!/usr/bin/python3
"""Define the city object"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city class

    Attributes:
    state_id(str): the state id
        name(str): The name of the city
    """
    state = ""
    name = ""
