from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) #map of map string -> ordereddict of time stamp -> value
        
        

    def set(self, key: str, value: str, timestamp: int):
        
        self.store[key].append([timestamp,value]) #key -> [(time1,value1), (time2,value2)]
        
    #modified_bsearch
    def bsearch (self, nums, start, end, target):
        if nums[end][0] <= target:
            return end
        
        while start + 1 < end:   #main difference
            mid = (start + end) // 2
            if target == nums[mid][0]:
                return mid
            elif target < nums[mid][0]:
                end = mid
            else:
                start = mid

        if nums[start][0] <= target:
            return start
        else:
            return -1
        

    def get(self, key: str, timestamp: int) -> str:
        nums = self.store[key]
        if not nums:
            return ''
        start, end = 0, len(nums) - 1
        
        ret = self.bsearch(nums, start, end, timestamp)
        if ret != -1:
            return nums[ret][1]
        else:
            return ''
        
        