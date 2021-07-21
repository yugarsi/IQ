#pivot index in array
class Solution(object):
    # can be done without modifying the initial array too

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            total += nums[i]

        leftsum = 0
        for i in range(len(nums)):
            if total - leftsum - nums[i] == leftsum:
                return i
            leftsum += nums[i]  # no need to do i-1
            # if below then lags behind!!!!!!!!!!!

        return -1