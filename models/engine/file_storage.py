#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

#circular imports


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        # TODO: should this be a copy()?
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        objname = obj.__class__.__name__
        obj = FileStorage.__objects["{}.{}".format(objname, obj.id)]
    

    def save(self):
        """Serialzes __objects to JSON file."""
        storing= FileStorage.__objects
        objectdict = {obj: storing[obj].to_dict() for obj in storing.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectdict, f)

    def reload(self):
        """derialiaztion of objects to the Json file __file_path"""
        try:
            with open(FileStorage.__file_path)as f:
                objectdict = json.load(f)
                for i in objectdict.values():
                    classname= i["__class__"]
                    del i["__class__"]
                    self.new(eval(classname)(**i))
        except FileNotFoundError:
            pass



    def attributes(self):
        """returns the valid attributes and their types for classnames"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}

        }
        return attributes
