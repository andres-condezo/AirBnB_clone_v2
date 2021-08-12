#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from models import storage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of City instances"""
            dict = storage.all(City)
            new_dict = []
            for value in dict.values():
                if self.id == value.state_id:
                    new_dict.append(value)
            return new_dict
