class MRUQueue:

    def __init__(self, n: int):
        self.store = []
        for i in range(1,n+1):
            self.store.append(i)
        
    #one solution
    def move_end(self, index):
        for i in range (index, len(self.store)-1):
            temp = self.store[i]
            self.store[i] = self.store[i+1]
            self.store[i+1] = temp
    
    #python list is double linked list
    def fetch(self, k: int) -> int:
        k -= 1
        v = self.store[k]
        del self.store[k]
        self.store.append(v)
        return v
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)