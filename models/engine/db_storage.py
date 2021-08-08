#!/usr/bin/python3
""" db_storage Module for HBNB project """
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage():
    """

    """
    __engine = None
    __session = None

    def __init__(self):
        """

        """

        env = os.environ.get('HBNB_ENV')
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_pwd = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                mysql_user,
                mysql_pwd,
                db_host,
                db,
            ), pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """

        """
        from models.state import State
        objList = {}
        if cls is None:
            query = self.__session.query(
                Amenity,
                City,
                Place,
                Review,
                State,
                User
            )
        else:
            query = self.__session.query(cls)

        for obj in query.all():
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objList[key] = obj
        return objList

    def new(self, obj):
        """

        """
        self.__session.add(obj)

    def save(self):
        """

        """
        self.__session.commit()

    def delete(self, obj=None):
        """

        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """

        """
        from models.state import State
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(session_factory)
        self.__session = Session()
