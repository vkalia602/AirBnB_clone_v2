#!/usr/bin/python3
'''
    This module defines DBStorage class
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import models
HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    '''
    Class DBStorage for database in MySQL
    Attributes:
    engine-
    session-
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Instantiate DBStorage
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True, echo=False)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Method that creates a query and prints a dictionary of cls
        '''
        obj_dict = {}
        print('db_all')
        if cls is not None:
            cls_obj = models.classes[cls]
            print('print class')
            for obj in self.__session.query(cls_obj):
                key = cls + '.' + obj.id
                obj_dict[key] = obj
        else:
            print('all tables')
            for cls_name in models.classes.values():
                try:
                    for obj in self.__session.query(cls_name):
                        key = cls_name + '.' + obj.id
                        obj_dict[key] = obj
                except:
                    pass
        return obj_dict

    def new(self, obj):
        '''
        Add a new object to database
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Save change to database
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Delete an object from database if not none
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
        To reload data from database
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
