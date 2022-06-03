#!/usr/bin/python3

class base:
    "python3 -c 'print(__import__("my_module").MyClass.__doc__)'"
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            __nb_objects == id
        else:
            __nb_objects += 1
