#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

if models.type_storage == 'db':
    Base = declarative_base()
else:
    Base = object

datef = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime\
                                        .strptime(kwargs['updated_at'], datef)
            if "created_at" in kwargs:
                kwargs['created_at'] = datetime\
                                        .strptime(kwargs['created_at'], datef)
            if "__cass__" in kwargs:
                del kwargs['__class__']

            self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key in self.__dict__.keys():
            if key == '_sa_instance_state':
                del(dictionary[key])
                break
        return dictionary

    def delete(self):
        """Delete the current instance"""
        models.storage.delete(self)
