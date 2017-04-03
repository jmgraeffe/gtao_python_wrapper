"""Python wrapper for GTA Orange's server functions

Subscribable built-in events:
+========+=========================+==================+
|  name  | vehicle-local arguments | global arguments |
+========+=========================+==================+
| unload | ???                     | ???              |
+--------+-------------------------+------------------+
"""
import __orange__
from GTAOrange import event as _event

__ehandlers = {}


def broadcast(text):
    """Broadcasts a message to all players.

    Args:
        text (str): message string
    """
    __orange__.Broadcast(text)


def on(event, cb):
    """Subscribes for an event.

    Args:
        event (string): event name
        cb (function): callback function
    """
    if event in __ehandlers.keys():
        __ehandlers[event].append(_event.Event(cb))
    else:
        __ehandlers[event] = []
        __ehandlers[event].append(_event.Event(cb))


def trigger(event, *args):
    """Triggers an event.

    Args:
        event (string): event name
        *args: arguments
    """
    if event in __ehandlers.keys():
        for handler in __ehandlers[event]:
            handler.getCallback()(*args)


def _onServerUnload(p0):
    trigger("unload", p0)


__orange__.AddServerEvent(_onServerUnload, "ServerUnload")
