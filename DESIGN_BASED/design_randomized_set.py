class RandomizedSet:

    def __init__(self):
        self.indexmap = {} #map of value to index (keys are sets element) key -> index of list
        self.elements = [] #list of elements All set keys are added here too
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        
        if val in self.indexmap:
            return False
        else:
            self.indexmap[val] = len(self.elements) 
            self.elements.append(val)
            return True

    def remove(self, val):
        if val not in self.indexmap:
            return False
        
        index = self.indexmap[val]
        last = self.elements[-1]
        
        self.elements[index] = last  #put last element in deleted place
        self.indexmap[last] = index #update index of last element
        
        self.elements.pop() #remove last element
        del self.indexmap[val]
        
        return True
            
    def getRandom(self):
        return choice(self.elements)
        # r = random.randint(0,len(self.elements)-1)
        # return self.elements[r]
        """
        Get a random element from the set.
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()