from __future__ import print_function
import builtins
import __orange__

def print(message):
    __orange__.Print(message)

builtins.print = print