# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

#binary_search in array of unknown length

class Solution(object):
    def bsearch(self, reader, start, end, target):
        while start <= end:
            mid = (start+end)//2
            if reader.get(mid) == target:
                return mid
            elif target < reader.get(mid):
                end = mid - 1
            else:
                start = mid + 1
                
        if reader.get(start) == 2147483647:
            return "max"
        return -1
    def search(self, reader, target):
        start = 0
        end = 2
        index = -1
        while index == -1:
            index = self.bsearch(reader, start, end, target)
            if index == "max":
                return -1
            else:
                start = end+1
                end = end * 2
        
        return index