#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """
                Getter attribute for cities
            """
            allCities = models.storage.all(City)
            stateCities = []

            for city in list(allCities.values()):
                if city.state_id == self.id:
                    stateCities.append(city)

            return stateCities
