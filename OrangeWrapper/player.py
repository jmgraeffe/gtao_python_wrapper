import GTAOrange as API
from OrangeWrapper import world as _world
from OrangeWrapper import event as _event
from OrangeWrapper import blip as _blip
from OrangeWrapper import marker as _marker

__pool = {}
__ehandlers = {}

class Player():

    id = None
    meta = {}
    
    _ehandlers = {}
    
    def __init__(self, id):
        self.id = id
        
    def attachBlip(self, name = None, scale = None, color = None, sprite = None):
        blip = _blip.create(name if name is not None else "Player", 0, 0, 0, scale if scale is not None else 1, color if color is not None else _blip.Color.ORANGE, sprite if sprite is not None else _blip.Sprite.STANDARD)
        blip.attachTo(self)
        return blip
        
    def createBlip(self, name, x, y, z, scale = None, color = None, sprite = None):
        return API.CreateBlipForPlayer(self.id, name, x, y, z, scale if scale is not None else 1, color if color is not None else _blip.Color.ORANGE, sprite if sprite is not None else _blip.Sprite.STANDARD)
    
    def createMarker(self, x, y, z, h = None, r = None, blip = None):
        marker = _marker.create(x, y, z, h if h is not None else 1, r if r is not None else 1)
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
        return API.GetPlayerHeading(self.id)
        
    def getID(self):
        return self.id
    
    def getModel(self):
        return API.GetPlayerModel(self.id)
    
    def getName(self):
        return API.GetPlayerName(self.id)
    
    def getPosition(self):
        return API.GetPlayerPosition(self.id)
    
    def getMoney(self):
        return API.GetPlayerMoney(self.id)
    
    def getHealth(self):
        return API.GetPlayerHealth(self.id)
    
    def giveWeapon(self, weapon, ammo = None):
        if ammo is None:
            return API.GivePlayerWeapon(self.id, weapon, 100)
        else:
            return API.GivePlayerWeapon(self.id, weapon, ammo)
            
    def isInMarker(self, marker):
        x1, y1, z1 = self.getPosition()
        x2, y2, z2 = marker.getPosition()
        
        return _world.getDistance(x1, y1, x2, y2) < 0.5 and (z1 - z2) * (z1 - z2) < (0.5 * 0.5)
    
    def removeWeapons(self):
        API.RemovePlayerWeapons(self.id)
    
    def on(self, event, cb):
        if event in __ehandlers[event].keys():
            self._ehandlers[event].append(_event.Event(cb))
        else:
            self._ehandlers[event] = []
            self._ehandlers[event].append(_event.Event(cb))
    
    def sendNotification(self, msg):
        API.SendPlayerNotification(self.id, msg)
    
    def chatMsg(self, msg):
        API.SendClientMessage(self.id, "{FFFFFF}" + msg, 255)
    
    def setArmour(self, armour):
        API.SetPlayerArmour(self.id, armour)
        
    def setHeading(self, heading):
        API.SetPlayerHeading(self.id, heading)
        
    def setHealth(self, health):
        API.SetPlayerHealth(self.id, health)
    
    def setName(self, name):
        API.SetPlayerName(self.id, name)
    
    def setInfoMsg(self, msg = None):
        if msg is None:
            API.SetPlayerInfoMsg(self.id, False)
        else:
            API.SetPlayerInfoMsg(self.id, msg)
    
    def setIntoVeh(self, veh, seat = None):
        if seat is None:
            API.SetPlayerIntoVehicle(self.id, veh.id, -1)
        else:
            API.SetPlayerIntoVehicle(self.id, veh.id, seat)
    
    def setModel(self, model):
        API.SetPlayerModel(self.id, model)
    
    def setPosition(self, x, y, z):
        API.SetPlayerPosition(self.id, x, y, z)
    
    def setMoney(self, money):
        API.SetPlayerMoney(self.id, money)
    
    def resetMoney(self):
        API.ResetPlayerMoney(self.id)
        
    def giveMoney(self, money):
        API.GivePlayerMoney(self.id, money)

    def giveAmmo(self, weapon, ammo):
        API.GivePlayerAmmo(self.id, weapon, ammo)
        
    def broadcast(self, msg, color):
        broadcast(msg, color)
    
    def disableHUD(self):
        API.DisablePlayerHud(self.id, True)
    
    def enableHUD(self):
        API.DisablePlayerHud(self.id, False)
    
    def trigger(self, event, *args):
        if event in self._ehandlers.keys():
            for handler in self._ehandlers[event]:
                handler.getCallback()(*args)
    
    def triggerClient(self, event, *args):
        API.ClientEvent(event, self.id, *args)

def broadcast(msg, color):
    API.BroadcastClientMessage(msg, color)
    
def exists(id):
    #TODO
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
    API.ClientEvent(event, -1, *args)

def _onConnect(*args):
    trigger("connect", *args)
    
def _onDisconnect(*args):
    trigger("disconnect", *args)

def _onCommand(*args):
    trigger("command", *args)

API.AddServerEvent(_onConnect, "PlayerConnect")
API.AddServerEvent(_onDisconnect, "PlayerDisconnect")
API.AddServerEvent(_onCommand, "PlayerCommand")