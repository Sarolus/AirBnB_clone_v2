#!/usr/bin/python3
""" Place Module for HBNB project """
from models.review import Review
from models.amenity import Amenity
import models
import os
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        association_table = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True
            ),
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True
            )
        )
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=association_table,
                                 backref='place_amenities', viewonly=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == "file":
        @property
        def reviews(self):
            """
                Getter attribute for reviews
            """
            allReviews = models.storage.all(Review)
            placeReviews = []

            for review in list(allReviews.values()):
                if review.place_id == self.id:
                    placeReviews.append(review)

            return placeReviews

        @property
        def amenities(self):
            """getter atribute amenities"""
            allAmenities = models.storage.all(Amenity)
            placeAmenities = []

            for objAmenity in list(allAmenities.values()):
                if objAmenity.place_id == self.id:
                    placeAmenities.append(objAmenity)

            return (placeAmenities)

        @amenities.setter
        def amenities(self, Obj):
            """amenities setter"""
            if isinstance(Obj, Amenity):
                self.amenity_ids.append(Obj.id)
