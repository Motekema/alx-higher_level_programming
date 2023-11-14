#!/usr/bin/python3

import json
import csv
import turtle

class Base:
    """
    Base model.

    Represents the base class for other classes in Project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.

        Args:
            id (int): The identity of the new Base. If None, it's automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be serialized.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            cls: The class.
            list_objs (list): A list of objects to be serialized and saved to a file.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class using a dictionary of attributes.

        Args:
            cls: The class.
            **dictionary (dict): Key-value pairs of attributes to initialize the object.

        Returns:
            object: An instance of the class with attributes set from the dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Load a list of class instances from a file containing JSON representations.

        Reads from '<cls.__name__>.json'.

        Returns:
            list: A list of class instances deserialized from the file.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.

        Args:
            cls: The class.
            list_objs (list): A list of objects to be serialized and saved to a CSV file.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                fieldnames = cls.get_fieldnames()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of class instances from a CSV file.

        Reads from '<cls.__name__>.csv'.

        Returns:
            list: A list of class instances deserialized from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls.get_fieldnames()
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [cls.convert_dict_values_to_int(d) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def get_fieldnames():
        """
        Get the field names for CSV serialization based on the class type.

        Returns:
            list: A list of field names appropriate for the class type.
        """
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @staticmethod
    def convert_dict_values_to_int(d):
        """
        Convert dictionary values to integers.

        Args:
            d (dict): Dictionary with string values to be converted.

        Returns:
            dict: Dictionary with integer values.
        """
        return dict([k, int(v)] for k, v in d.items())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.

        Returns:
            None
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

