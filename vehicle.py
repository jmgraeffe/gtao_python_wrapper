import __orange__
from GTAOrange import world as _world
from GTAOrange import blip as _blip
from GTAOrange import text as _text
from GTAOrange import player as _player
from GTAOrange import event as _event

__pool = {}
__ehandlers = {}

# attachOwnText
# attachOwnBlip


class Vehicle():

    id = None
    meta = {}
    texts = {}

    _ehandlers = {}

    def __init__(self, id):
        self.id = id

    def attachBlip(self, name="Vehicle", scale=0.6, color=_blip.Color.ORANGE, sprite=_blip.Sprite.PERSONALVEHICLECAR):
        blip = _blip.create(name, 0, 0, 0, scale, color, sprite)
        blip.attachTo(self)
        return blip

    def attachText(self, text, x=0, y=0, z=0, tcolor=0xFFFFFFFF, ocolor=0xFFFFFFFF, size=20):
        txt = _text.create(text, 0, 0, 72, tcolor, ocolor, size)
        txt.attachToVeh(self, x, y, z)
        self.texts[txt.id] = txt

        return txt

    def delete(self):
        deleteByID(self.id)

    def distanceTo(self, x, y, z=None):
        if z is not None:
            x1, y1, z1 = self.getPosition()
            return _world.getDistance(x1, y1, z1, x, y, z)
        else:
            x1, y1 = self.getPosition()
            return _world.getDistance(x1, y1, x, y)

    def getID(self):
        return self.id

    def getPosition(self):
        return __orange__.GetVehiclePosition(self.id)

    def equals(self, veh):
        if isinstance(veh, Vehicle):
            return self.id == veh.id
        else:
            return False

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


def create(model, x, y, z, h):
    veh = Vehicle(__orange__.CreateVehicle(model, x, y, z, h))
    __pool[veh.id] = veh
    return veh


def deleteByID(id):
    global __pool

    if isinstance(id, int):
        if exists(id):
            if id in __pool.keys():
                del __pool[id]
            return __orange__.DeleteVehicle(id)
        return False
    else:
        raise TypeError('Vehicle ID must be an integer')


def exists(id):
    # return __orange__.VehicleExists(id)
    return True


def getByID(id):
    global __pool

    if isinstance(id, int):
        if exists(id):
            if id not in __pool.keys():
                __pool[id] = Vehicle(id)
            return __pool[id]
        return False
    else:
        raise TypeError('Vehicle ID must be an integer')


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


def _onPlayerEntered(player_id, vehicle_id):
    player = _player.getByID(player_id)
    vehicle = getByID(vehicle_id)

    trigger("playerentered", player, vehicle)
    vehicle.trigger("playerentered", player)
    _player.trigger("playerentered", player, vehicle)
    player.trigger("playerentered", vehicle)


def _onPlayerLeft(player_id, vehicle_id):
    player = _player.getByID(player_id)
    vehicle = getByID(vehicle_id)

    trigger("playerleft", player, vehicle)
    vehicle.trigger("playerleft", player)
    _player.trigger("leftvehicle", player, vehicle)
    player.trigger("leftvehicle", vehicle)


__orange__.AddServerEvent(_onPlayerEntered, "EnterVehicle")
__orange__.AddServerEvent(_onPlayerLeft, "LeftVehicle")
