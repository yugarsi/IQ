class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        While curr <= p2 :

If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.

If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.

If nums[curr] = 1 : move pointer curr to the right.