import __orange__
from GTAOrange import world
from GTAOrange import event as _event
from GTAOrange import vehicle as _vehicle
from GTAOrange import player as _player

__pool = {}
__ehandlers = {}

class Marker():
    
    id = None
    x = None
    y = None
    z = None
    h = None
    r = None
    
    _ehandlers = {}
    _players = {}
    
    def __init__(self, id, x, y, z, h, r):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.r = r
    
    def delete(self):
        deleteByID(self.id)
    
    def distanceTo(self, x, y, z = None):
        if z is not None:
            x1, y1, z1 = self.getPosition()
            return _world.getDistance(x1, y1, z1, x, y, z)
        else:
            x1, y1 = self.getPosition()
            return _world.getDistance(x1, y1, x, y)
    
    def getID(self):
        return self.id
    
    def getPosition(self):
        return (self.x, self.y, self.z)
    
    def on(self, event, cb):
        if event in self._ehandlers.keys():
            self._ehandlers[event].append(_event.Event(cb))
        else:
            self._ehandlers[event] = []
            self._ehandlers[event].append(_event.Event(cb))
    
    def trigger(self, event, *args):
        if event in self._ehandlers.keys():
            for handler in self._ehandlers[event]:
                handler.getCallback()(self, *args)
    
def create(x, y, z, h = 1, r = 1, blip = None):
    from GTAOrange import blip as _blip
    global __pool
    
    marker = Marker(__orange__.CreateMarkerForAll(x, y, z, h, r), x, y, z, h, r)
    __pool[marker.id] = marker
    
    if blip is not None:
        marker.blip = _blip.create("Marker", x, y, z)
    
    return marker

def deleteByID(id):
    global __pool
    
    if isinstance(id, int):
        if id in __pool.keys():
            del __pool[id]
            return __orange__.DeleteMarker(id)
        else:
            return False
    else:
        raise TypeError('Marker ID must be an integer')
        
def getByID(id):
    global __pool
    
    if isinstance(id, int):
        if id in __pool.keys():
            return __pool[id]
        return False
    else:
        raise TypeError('Marker ID must be an integer')

def getAll():
    return __pool

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

def _onPlayerEnteredMarker(player_id, marker_id):
    player = _player.getByID(player_id)
    marker = getByID(marker_id)
    
    trigger("playerentered", player)
    marker.trigger("playerentered", player)
    _player.trigger("enteredmarker", marker)
    player.trigger("enteredmarker", marker)

def _onPlayerLeftMarker(player_id, marker_id):
    player = _player.getByID(player_id)
    marker = getByID(marker_id)
    
    trigger("playerleft", player)
    marker.trigger("playerleft", player)
    _player.trigger("leftmarker", marker)
    player.trigger("leftmarker", marker)

def _onVehicleEnteredMarker(vehicle_id, marker_id):
    vehicle = _vehicle.getByID(vehicle_id)
    marker = getByID(marker_id)
    
    trigger("vehicleentered", vehicle)
    marker.trigger("vehicleentered", vehicle)
    _vehicle.trigger("enteredmarker", marker)
    vehicle.trigger("enteredmarker", marker)

def _onVehicleLeftMarker(vehicle_id, marker_id):
    vehicle = _vehicle.getByID(vehicle_id)
    marker = getByID(marker_id)
    
    trigger("vehicleleft", vehicle)
    marker.trigger("vehicleleft", vehicle)
    _vehicle.trigger("leftmarker", marker)
    vehicle.trigger("leftmarker", marker)
    
__orange__.AddServerEvent(_onPlayerEnteredMarker, "EnterMarker")
__orange__.AddServerEvent(_onPlayerLeftMarker, "LeftMarker")
__orange__.AddServerEvent(_onVehicleEnteredMarker, "VehEnterMarker")
__orange__.AddServerEvent(_onVehicleLeftMarker, "VehLeftMarker")