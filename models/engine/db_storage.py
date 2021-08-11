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
        This class manages storage of hbnb models in DB.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            Initialize the DBStorage Class
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

        if env == 'test' and db == 'hbnb_test_db':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Return a dictionary of all objects
            from a class present in the database.
        """
        from models.state import State
        objList = {}
        if type(cls) == str:
            cls = eval(cls)
        if cls is None:
            for cls in (Amenity, City, Place, Review, State, User):
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objList[key] = obj
        else:
            query = self.__session.query(cls)

            for obj in query.all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objList[key] = obj

        return objList

    def new(self, obj):
        """
            Adds a new object to the database
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Deletes an object from the database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            Initialize all tables of the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
