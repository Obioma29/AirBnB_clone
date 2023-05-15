#!/usr/bin/python3
"""
This File defines the BaseModel class that will
serve as the base class for all our models."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of self"""

        fmt = "[{}] ({}) {}"
        return fmt.format(type(self).__name__, self.id,
                self.__dict__)

    def save(self):
        """updates last updated variable"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of self"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.isoformat()
        temp['updated_at'] = self.updated_at.isoformat()
        return temp
