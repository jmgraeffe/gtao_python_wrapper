import __orange__
from GTAOrange import world as _world
from GTAOrange import event as _event

__pool = {}
__ehandlers = {}

#attachOwnBlip

class Player():

    id = None
    meta = {}
    
    _ehandlers = {}
    
    def __init__(self, id):
        self.id = id
        
    def attachBlip(self, name = "Player", scale = 1, color = None, sprite = None):
        from GTAOrange import blip as _blip
        
        blip = _blip.create(name, 0, 0, 0, scale, color if color is not None else _blip.Color.ORANGE, sprite if sprite is not None else _blip.Sprite.STANDARD)
        blip.attachTo(self)
        return blip
        
    def createBlip(self, name, x, y, z, scale = 1, color = None, sprite = None):
        from GTAOrange import blip as _blip
        return __orange__.CreateBlipForPlayer(self.id, name, x, y, z, scale, color if color is not None else _blip.Color.ORANGE, sprite if sprite is not None else _blip.Sprite.STANDARD)
    
    def createMarker(self, x, y, z, h = 1, r = 1, blip = None):
        from GTAOrange import marker as _marker
    
        marker = _marker.create(x, y, z, h, r)
        if blip is not None:
            m.blip = self.createBlip("Marker", x, y, z)
        return marker
    
    def distanceTo(self, x, y, z = None):
        if z is None:
            x1, y1, z1 = self.getPosition()
            return _world.getDistance(x1, y1, z1, x, y, z)
        else:
            x1, y1 = self.getPosition()
            return _world.getDistance(x1, y1, x, y)
    
    def getHeading(self):
        return __orange__.GetPlayerHeading(self.id)
        
    def getID(self):
        return self.id
    
    def getModel(self):
        return __orange__.GetPlayerModel(self.id)
    
    def getName(self):
        return __orange__.GetPlayerName(self.id)
    
    def getPosition(self):
        return __orange__.GetPlayerPosition(self.id)
    
    def getMoney(self):
        return __orange__.GetPlayerMoney(self.id)
    
    def getHealth(self):
        return __orange__.GetPlayerHealth(self.id)
    
    def giveWeapon(self, weapon, ammo = None):
        if ammo is None:
            return __orange__.GivePlayerWeapon(self.id, weapon, 100)
        else:
            return __orange__.GivePlayerWeapon(self.id, weapon, ammo)
            
    def isInMarker(self, marker):
        x1, y1, z1 = self.getPosition()
        x2, y2, z2 = marker.getPosition()
        
        return _world.getDistance(x1, y1, x2, y2) < 0.5 and (z1 - z2) * (z1 - z2) < (0.5 * 0.5)
    
    def removeWeapons(self):
        __orange__.RemovePlayerWeapons(self.id)
    
    def on(self, event, cb):
        if event in __ehandlers[event].keys():
            self._ehandlers[event].append(_event.Event(cb))
        else:
            self._ehandlers[event] = []
            self._ehandlers[event].append(_event.Event(cb))
    
    def sendNotification(self, msg):
        __orange__.SendPlayerNotification(self.id, msg)
    
    def chatMsg(self, msg):
        __orange__.SendClientMessage(self.id, "{FFFFFF}" + msg, 255)
    
    def setArmour(self, armour):
        __orange__.SetPlayerArmour(self.id, armour)
    
    def setHeading(self, heading):
        __orange__.SetPlayerHeading(self.id, heading)
        
    def setHealth(self, health):
        __orange__.SetPlayerHealth(self.id, health)
    
    def setName(self, name):
        __orange__.SetPlayerName(self.id, name)
    
    def setInfoMsg(self, msg = None):
        if msg is None:
            __orange__.UnsetInfoMsg(self.id)
        else:
            __orange__.SetInfoMsg(self.id, msg)
    
    def setIntoVeh(self, veh, seat = None):
        if seat is None:
            __orange__.SetPlayerIntoVehicle(self.id, veh.id, -1)
        else:
            __orange__.SetPlayerIntoVehicle(self.id, veh.id, seat)
    
    def setModel(self, model):
        __orange__.SetPlayerModel(self.id, model)
    
    def setPosition(self, x, y, z):
        __orange__.SetPlayerPosition(self.id, x, y, z)
    
    def setMoney(self, money):
        __orange__.SetPlayerMoney(self.id, money)
    
    def resetMoney(self):
        __orange__.ResetPlayerMoney(self.id)
        
    def giveMoney(self, money):
        __orange__.GivePlayerMoney(self.id, money)

    def giveAmmo(self, weapon, ammo):
        __orange__.GivePlayerAmmo(self.id, weapon, ammo)
        
    def broadcast(self, msg, color):
        broadcast(msg, color)
    
    def disableHUD(self):
        __orange__.DisablePlayerHud(self.id, True)
    
    def enableHUD(self):
        __orange__.DisablePlayerHud(self.id, False)
    
    def trigger(self, event, *args):
        if event in self._ehandlers.keys():
            for handler in self._ehandlers[event]:
                handler.getCallback()(*args)
    
    def triggerClient(self, event, *args):
        __orange__.TriggerClientEvent(self.id, event, *args)

def broadcast(msg, color):
    __orange__.BroadcastClientMessage(msg, color)
    
def exists(id):
    #return __orange__.PlayerExists(id)
    return True
    
def deleteByID(id):
    global __pool
    del __pool[id]

def getByID(id):
    global __pool
    
    if isinstance(id, int):
        if exists(id):
            if id not in __pool.keys():
                __pool[id] = Player(id)
            return __pool[id]
        else:
            return False
    else:
        raise TypeError('Player ID must be an integer')

def getByName(name):
    for key, player in __pool.items():
        if player.getName() == name:
            return player
    return False

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

def triggerClient(event, *args):
    __orange__.TriggerClientEvent(-1, event, *args)

def _onConnect(*args):
    # replace first arg (player id) with player obj
    args = list(args)
    args[0] = getByID(args[0])
    
    trigger("connect", *args)
    
def _onDisconnect(*args):
    # replace first arg (player id) with player obj
    args = list(args)
    args[0] = getByID(args[0])
    
    trigger("disconnect", *args)

def _onCommand(*args):
    # replace first arg (player id) with player obj
    args = list(args)
    args[0] = getByID(args[0])
    
    trigger("command", *args)

__orange__.AddServerEvent(_onConnect, "PlayerConnect")
__orange__.AddServerEvent(_onDisconnect, "PlayerDisconnect")
__orange__.AddServerEvent(_onCommand, "PlayerCommand")