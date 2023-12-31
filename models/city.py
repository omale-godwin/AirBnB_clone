#!/usr/bin/python3
"""Define the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city

    Attributes:
        state_id (str): State id
        name (str): State name
    """
    state_id: str = ""
    name: str = ""
