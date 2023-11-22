#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Parameters:
            *args: Variable-length argument list (not used in this method).
            **kwargs: Variable-length keyword argument list.

        Keyword Arguments:
            id (str): Unique identifier for the BaseModel instance.
            created_at (datetime): Datetime representing the creation time.
            updated_at (datetime): Datetime representing the last update time.
            __class__ (str): Class information

        If no kwargs are provided:
            - Initialize default values for id, created_at, and updated_at.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "create_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

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

        if '_sa_instance_state' in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def delete(self):
        """deletes current instance from the storage"""
        return models.storage.delete(self)
