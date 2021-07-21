#check alien dictionary is lexicographically sorted
class Solution(object):
    # checking something is sorted or not can be done in o(n)
    # actually sorting an array is o(nlog(n))
    def checkInOrder(self, a, b, ordermap):
        i = 0
        while i< min(len(a),len(b)):
            if ordermap[a[i]] < ordermap[b[i]]:
                return True
            elif ordermap[a[i]] > ordermap[b[i]]:
                return False
            else:
                i+=1
        return len(a) <= len(b)
        
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ordermap = {}
        i = 0
        for i in range (len(order)):
            ordermap[order[i]] = i
        
        for i in range(len(words)-1):
            if(self.checkInOrder(words[i], words[i+1], ordermap) == False):
                return False
        
        return True
        