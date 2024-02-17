#!/usr/bin/python3
""" import the sys module """
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def lists(argument):
    """ add arguments to a list"""
    try:
        value = load("add_item.json")
    except FileNotFoundError:
        value = []

    value += argument
    save(value, "add_item.json")


argument = sys.argv[1:]
lists(argument)