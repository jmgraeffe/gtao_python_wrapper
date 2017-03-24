import threading

__pool = {}
__current = 0

class Thread(threading.Thread):

    id = None
    
    _function = None
    
    def __init__(self, f):
        global __current
        
        threading.Thread.__init__(self) 
        self.id = __current
        self._function = f
        
        __current += 1