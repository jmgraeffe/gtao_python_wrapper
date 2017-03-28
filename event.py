__pool = {}
_current = 0

class Event():

    id = None
    
    _cb = None
    
    def __init__(self, cb):
        global _current
        
        self._cb = cb
        self.id = _current
        
        _current += 1
    
    def getCallback(self):
        return self._cb
    
    def cancel(self):
        pass