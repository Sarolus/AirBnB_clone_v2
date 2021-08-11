#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from unittest.case import skipIf
import os


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != file,
        "File storage tests only"
    )
    def test_name2(self):
        """ """
        new = self.value()
        new.name = "San Francisco"
        self.assertIn("'name': '{}'".format(new.name), str(new))
        # self.assertEqual(type(new.name), str)
