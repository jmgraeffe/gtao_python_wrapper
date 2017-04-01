"""Debugging library for the GTA Orange Python wrapper
"""
__author__ = "Jon-Mailes Graeffe"
__copyright__ = "Copyright 2017, Jon-Mailes Graeffe"
__credits__ = ["GTA Orange team", "Hexaflexagon"]
__license__ = "Closed-source, freeware"
__maintainer__ = "Jon-Mailes Graeffe"

def dump(obj, magic=False):
    """Dumps every attribute of an object to the console.

    Args:
        obj (any object): object you want to dump
        magic (bool, optional): True if you want to output "magic" attributes (like __init__, ...)
    """
    for attr in dir(obj):
        if magic is True:
            print("obj.%s = %s" % (attr, getattr(obj, attr)))
        else:
            if not attr.startswith('__'):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
