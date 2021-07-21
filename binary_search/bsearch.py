class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end: #have to check until start==end
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid-1  #end = mid -1 as we are done checking mid or else will lead to inf loop
            else:
                start = mid+1 #mid +1 as we are done checkin mid
        return -1