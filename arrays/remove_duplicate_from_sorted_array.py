class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # [ 1,2,3,4,3,3,3,4]
        i = 0 
        j = 1
        while j < len(nums): #end condition
            if (nums[i] != nums[j]):
                i+=1
                nums[i] = nums[j] 
            j+=1
        
        return i+1