import __orange__

__ehandlers = {}

def broadcast(text):
    __orange__.Broadcast(text)

def on(event, cb):
    if event in __ehandlers.keys():
        __ehandlers[event].append(_event.Event(cb))
    else:
        __ehandlers[event] = []
        __ehandlers[event].append(_event.Event(cb))

def trigger(event, *args):
    if event in __ehandlers.keys():
        for handler in __ehandlers[event]:
            handler.getCallback()(*args)

def _onServerUnload(p0):
    trigger("unload", p0)
    
__orange__.AddServerEvent(_onPlayerEntered, "ServerUnload")