class ConnectionManager:
    def __init__(self, limit):
        self.limit = limit
        self.allocated = 0
        self.freelist = []
        self.m = threading.RLock()
        self.obj_available = threading.Condition(self.m)

    def freeObject(obj):
        if obj is None:
            return
                          
        self.m.acquire()
        self.freelist.append(obj)
        self.obj_available.notify()
        self.m.release()    
    
    def getObject():
        self.m.acquire()
        obj = None
        while len(self.freelist) == 0 and self.allocated == self.limit:
            self.obj_available.wait()

        if len(self.freelist):
            obj = self.freelist.pop()
        self.m.release()    

        if obj is None:
            obj = createObject()
        return obj

cm = ConnectionManager(5)
obj = cm.getObject()
cm.freeObject(obj)
