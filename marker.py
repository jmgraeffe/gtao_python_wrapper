import __orange__ as API
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
        API.DeleteMarker(self.id)
        del __pool[self.id]
    
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
        if event in __ehandlers[event].keys():
            self._ehandlers[event].append(_event.Event(cb))
        else:
            self._ehandlers[event] = []
            self._ehandlers[event].append(_event.Event(cb))
    
    def trigger(self, event, *args):
        if event in self._ehandlers.keys():
            for handler in self._ehandlers[event]:
                handler.getCallback()(*args)
    
def create(x, y, z, h = 1, r = 1, blip = None):
    from GTAOrange import blip as _blip
    global __pool
    
    marker = Marker(API.CreateMarkerForAll(x, y, z, h, r), x, y, z, h, r)
    __pool[marker.id] = marker
    
    if blip is not None:
        marker.blip = _blip.create("Marker", x, y, z)
    
    return marker

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
    _player.trigger("enteredmarker", marker)

def _onPlayerLeftMarker(player_id, marker_id):
    player = _player.getByID(player_id)
    marker = getByID(marker_id)
    
    trigger("playerleft", player)
    _player.trigger("leftmarker", marker)

def _onVehicleEnteredMarker(vehicle_id, marker_id):
    vehicle = _vehicle.getByID(vehicle_id)
    marker = getByID(marker_id)
    
    trigger("vehicleentered", vehicle)
    _vehicle.trigger("enteredmarker", marker)

def _onVehicleLeftMarker(vehicle_id, marker_id):
    vehicle = _vehicle.getByID(vehicle_id)
    marker = getByID(marker_id)
    
    trigger("vehicleleft", vehicle)
    _vehicle.trigger("leftmarker", marker)
    
API.AddServerEvent(_onPlayerEnteredMarker, "EnterMarker")
API.AddServerEvent(_onPlayerLeftMarker, "LeftMarker")
API.AddServerEvent(_onVehicleEnteredMarker, "VehEnterMarker")
API.AddServerEvent(_onVehicleLeftMarker, "VehLeftMarker")