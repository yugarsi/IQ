class Solution:
    ##solution to get sorted result but works only for distinct numbers
    #returns repeated for
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set() #no need of set if all elements are unique
        nums.sort()
        target = 0
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1  #note initialize inside the loop
            while(left < right):
                tsum = nums[i] + nums[left] + nums[right]
                if tsum == target:
                    rtuple = (nums[i], nums[left], nums[right])
                    res.add(rtuple)
                    left +=1
                    right -=1
                if tsum < target:
                    left +=1
                if tsum > target:
                    right-=1
                    
        return list(res)