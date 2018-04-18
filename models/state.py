#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import city
from os import getenv
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state',
                              cascade='delete')
    else:
        @property
        def cities(self):
            '''
            Getter for cities
            '''
            all_cities = models.storage.all(models.classes["City"])
            cities = []
            for key, obj in all_cities.items():
                if obj.state_id == self.id:
                    cities.append(obj)
            return cities
