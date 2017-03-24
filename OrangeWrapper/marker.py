import GTAOrange as API
from OrangeWrapper import world

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
    
    def delete():
        pass
    
    def distanceTo(x, y, z):
        pass
    
    def getID():
        pass
    
    def getPosition():
        pass
    
    def on(event, cb):
        pass
    
    def trigger(event, params):
        pass
    
def create(x, y, z, h, r, blip = None):
    pass

def exists(id):
    pass

def getByID(id):
    pass

def on(event, cb):
    pass

def trigger(event, params):
    pass