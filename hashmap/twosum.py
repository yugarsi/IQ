class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hmap:
                return[i, hmap[nums[i]]]
            else:
                hmap[diff] = i
        
        return []
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap:
                return[i, hmap[diff]]
            else:
                hmap[nums[i]] = i
        
        return []

    #facebook number of ways count all pairs even if repeated
    def numberOfWays(arr, k):
    if not arr:
        return 0
        maps = {} #save hashmap and count
        counter = 0
        for num in arr:
            diff = k - num
            if diff in maps:
                counter += maps[diff] #cumulative sum give NC2
                maps[diff] += 1
            else:
                maps[num] = 1
        return counter

    #count pairs brute force
    def numberOfWays(arr, k):
        if not arr:
            return 0
        counter = 0
        for i in range(len(arr)):
          for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
              counter += 1
        
        return counter