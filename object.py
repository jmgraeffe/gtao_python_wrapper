import __orange__
from GTAOrange import world

__pool = {}
__ehandlers = {}

class Object():

    id = None
    
    _ehandlers = {}
    
    def __init__(self, id):
        self.id = id
        
    def delete(self):
        deleteByID(self.id)
    
    def getID(self):
        return self.id
    
    def equals(self, obj):
        if isinstance(obj, Object):
            return self.id == veh.id
        else:
            return False
    
def create(model, x, y, z, pitch, yaw, roll):
    global __pool
    
    object = Object(__orange__.CreateObject(model, x, y, z, pitch, yaw, roll))
    __pool[object.id] = object
    return object
    
def deleteByID(id):
    global __pool
    
    if isinstance(id, int):
        if id in __pool.keys():
            del __pool[id]
            return __orange__.DeleteObject(id)
        else:
            return False
    else:
        raise TypeError('Object ID must be an integer')
        
def getByID(id):
    global __pool
    
    if isinstance(id, int):
        if id in __pool.keys():
            return __pool[id]
        return False
    else:
        raise TypeError('Object ID must be an integer')

def getAll():
    return __pool