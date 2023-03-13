#!/usr/bin/python3
"""Define the amenity object"""
from models.base_model import BaseModel


class Place(BaseModel):
    """the description of a place

    Attributes:
        city_id(str): the city id of the place
        user_id(str): the user id
        name(str): the name the place
        description(str): the description of the place
        number_room(int): the number of the place
        number_bathroom(int): the number of bathroom
        max_guest_rooms(int): the maximum number of guest rooms
        price_by_night(int): the price of the hotel by night
        latitude(float): the latitude
        longitude(float): the longitude
        amenity_ids(list): the amenities in that place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
