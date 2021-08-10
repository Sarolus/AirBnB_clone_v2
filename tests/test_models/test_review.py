#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from unittest.case import skipIf
from models.review import Review
import unittest
import os


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_place_id(self):
        """ """
        new = self.value()
        new.place_id = "toto"
        self.assertIn("'place_id': '{}'".format(new.place_id), str(new))
        # self.assertEqual(type(new.place_id), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_user_id(self):
        """ """
        new = self.value()
        new.user_id = "toto"
        self.assertIn("'user_id': '{}'".format(new.user_id), str(new))
        # self.assertEqual(type(new.user_id), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_text(self):
        """ """
        new = self.value()
        new.text = "toto"
        self.assertIn("'text': '{}'".format(new.text), str(new))
        # self.assertEqual(type(new.text), str)
