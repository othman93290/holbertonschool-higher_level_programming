#!/usr/bin/python3
"""import json module"""
import json


def load_from_json_file(filename):
    """create an Object from a JSON file"""
    with open(filename, "r") as file:
        load_obj = json.load(file)
        return load_obj