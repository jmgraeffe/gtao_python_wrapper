__pool = {}
__current = 0

class Text():

    id = None
    
    _cb = None
    
    def __init__(self, cb):
        global __current
        
        self._cb = cb
        self.id = __current
        
        __current += 1
    
    def cb(params):
        pass
    
    def cancel():
        pass