import __orange__
from GTAOrange import world

__pool = {}
__ehandlers = {}

class Object():

    id = None
    meta = {}
    texts = {}
    
    _ehandlers = {}
    
    def __init__(self, id):
        self.id = id
    
    def getID(self):
        pass
    
    def isObject(self, obj):
        pass
    
def create(model, x, y, z, h):
    pass

def getByID(id):
    pass