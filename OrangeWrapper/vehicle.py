import GTAOrange as API

__pool = {}
__ehandlers = {}

class Vehicle():

    id = None
    meta = {}
    
    def __init__(self, id):
        self.id = id
    
    def attachBlip(self, name, scale, color, sprite):
        pass
    
    def attachText(self, text, x, y, z, tcolor, ocolor, size):
        pass
    
    def distanceTo(self, x, y, z):
        pass
    
    def getID(self):
        pass
    
    def getPosition(self):
        pass
    
    def isVehicle(self, veh):
        pass
    
    def on(self, event, cb):
        pass
    
    def trigger(self, event, params):
        pass
    
def create(model, x, y, z, h):
    pass

def exists(id):
    pass

def getByID(id):
    pass

def on(event, cb):
    pass

def trigger(event, params):
    pass