class Solution:
    #if repeated this pivot solution won't work
    #ascending and rotated sorted
    # [4,5,6,7,0,1,2]
    def search(self, nums, target):
        
        def bsearch(left, right, target):    
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1    
        
        #this won't work when left == right i.e just one element
        #find where the rotation index is
        def find_pivot(left, right):
            if nums[left] < nums[right]:   #if first < last then it's not rotated
                return 0
            
            # [4,5,6,7,0,1,2] #everwhere mid < mid+1 as it's sorted except pivot
            while left <= right:
                mid = (left + right)//2
                if nums[mid] > nums[mid+1]:  #if mid > mid+1 element that means pivot = mid+1
                    return mid+1
                
                elif nums[mid] >= nums[left]: #pivot will be on the right
                    left = mid + 1
                else:#pivot will be on the left
                    right = mid - 1  
                
        
        n = len(nums)
        if n == 1:
            return 0 if target == nums[0] else -1 # if n==1 finding pivot won't work
        pivot= find_pivot(0 , n-1)
        print(pivot)
        
        if pivot == 0:
            return bsearch(0 , n-1, target)
        
        if target < nums[0]: #if target < first binary_search in right part
            return bsearch(pivot, len(nums)-1, target)
        
        return bsearch(0, pivot-1, target) #else binary_search left part

            
    
                    

####1 pass solution

class Solution:
    def search(self, nums: List[int], target: int):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:   ## still in ascending order
                if target >= nums[start] and target < nums[mid]:  #binary_search like in ascending order
                    end = mid - 1
                else:
                    start = mid + 1
            else:                                              ##if reversed
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
