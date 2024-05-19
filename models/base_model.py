#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime, timezone


class BaseModel:

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        class_name = self.__class__.__name__
        return f"class_mame: {class_name}\nid = {self.id}\ncontent : {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()

        return dictionary
