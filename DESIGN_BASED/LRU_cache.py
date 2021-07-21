#put operation

#Use an ordered dictionary
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict() #internally linkedhashmap
        

    def get(self, key):
        if key in self.cache:       #move to end not available in 
            self.cache.move_to_end(key) #move to end => most recently accessed
            return self.cache[key]
        return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.size: #This implies cache
            self.cache.popitem(last = False) #remove the first item (i.e. last used )
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)