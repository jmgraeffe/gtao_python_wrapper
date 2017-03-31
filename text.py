__pool = {}

class Text():
    
    id = None
    x = None
    y = None
    z = None
    tcolor = None
    ocolor = None
    size = None
    
    _ehandlers = {}
    
    def __init__(self, id, text, x, y, z, tcolor = 0xFFFFFFFF, ocolor = 0xFFFFFFFF, size = 20):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.tcolor = tcolor
        self.ocolor = ocolor
        self.size = size
    
    def delete(self):
        API.Delete3DText(self.id)
        del __pool[self.id]
        
    def getID(self):
        return self.id
    
    def getPosition(self):
        return (self.x, self.y, self.z)
    
    def getColors(self):
        return (self.tcolor, self.ocolor)
    
    def getSize(self):
        return self.size
    
    def getText(self):
        return self.text
    
def create(text, x, y, z, tcolor = 0xFFFFFFFF, ocolor = 0xFFFFFFFF, size = 20):
    global __pool
    
    text = Text(API.Create3DText(text, x, y, z, tcolor, ocolor, size), text, x, y, z, tcolor, ocolor, size)
    __pool[text.id] = text
    return text
    
def getByID(id):
    global __pool
    
    if isinstance(id, int):
        if id in __pool.keys():
            return __pool[id]
        return False
    else:
        raise TypeError('3DText ID must be an integer')

def getAll():
    return __pool