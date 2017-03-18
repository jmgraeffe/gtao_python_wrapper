import GTAOrange as API
from OrangeWrapper import world

__pool = {}
__ehandlers = {}

class Player():

    id = None
    
    def __init__(self, id):
        self.id = id
        
    def attachBlip(self, name, scale, color, sprite):
        pass
    
    def createBlip(self, name, x, y, z, scale, color, sprite):
        pass
    
    def createMarker(self, x, y, z, h, r, blip):
        pass
    
    def distanceTo(self, x, y, z = None):
        if z is None:
            x1, y1, z1 = self.getPosition()
            return world.getDistance(x1, y1, z1, x, y, z)
        else:
            x1, y1 = self.getPosition()
            return world.getDistance(x1, y1, x, y)
    
    def getHeading(self):
        return API.GetPlayerHeading(self.id)
        
    def getID(self):
        return self.id
    
    def getModel():
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
            
    def isInMarker(self, m):
        pass
    
    def removeWeapons(self):
        API.RemovePlayerWeapons(self.id)
    
    def on(self, event, cb):
        if event in __ehandlers[event].keys():
            __ehandlers[event].append(cb)
        else:
            __ehandlers[event] = []
            __ehandlers[event].append(cp)
    
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
    
    def trigger(self, event, params):
        pass

def broadcast(msg, color):
    API.BroadcastClientMessage(msg, color)
    
def exists(id):
    #TODO
    return True

def deleteByID(id):
    del __pool[id]

def getByID(id):
    if id in __pool.keys():
        return __pool[id]
    elif isinstance(id, int) and exists(id):
        __pool[id] = Player(id)
        return __pool[id]
    else:
        raise TypeError('Player ID must be an integer')

def getByName(name):
    for key, player in __pool.items():
        if player.getName() == name:
            return player
    return False

def on(event, cb):
    if event in __ehandlers.keys():
        __ehandlers[event].append(cb)
    else:
        __ehandlers[event] = []
        __ehandlers[event].append(cb)

def trigger(event, params):
    pass

def triggerClient(event, params):
    pass

def _onConnect(player, ip):
    if "connect" in __ehandlers.keys():
        for cb in __ehandlers["connect"]:
            cb(player, ip)

def _onDisconnect(player, reason):
    if "disconnect" in __ehandlers.keys():
        for cb in __ehandlers["disconnect"]:
            cb(player, reason)


def _onCommand(player, command):
    if "command" in __ehandlers.keys():
        for cb in __ehandlers["command"]:
            cb(player, command)

API.AddServerEvent(_onConnect, "PlayerConnect")
API.AddServerEvent(_onDisconnect, "PlayerDisconnect")
API.AddServerEvent(_onCommand, "PlayerCommand")