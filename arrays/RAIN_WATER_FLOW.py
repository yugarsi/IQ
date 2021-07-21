'''
Trap rain water flow
Algorithm using two pointers
1. init left = 0 and right = len(arr) - 1
2. initialize leftmax and rightmax to 0, i.e. tallest to the left and right
3. if arr[left] < arr[right] .. i.e. right is taller and water won't flow out
    update leftmax if arr[left] >= leftmax (no extra water counted here)
    else result = result + (leftmax-height) ,*note leftmax-height is water level

4. do the same for right pointer when arr[left] > arr[right] i.e. water won't flowout of left

'''

class Solution:
    # O(N^2 is brute force)
    # O(N) time and O(1) space solution most optimal
    def trap(self, height) -> int:
        # init left and right pointers
        left = 0
        right = len(height) - 1
        #initialize max
        leftmax, rightmax = 0, 0

        res = 0
        while (left < right):
            if height[left] < height[right]:  # right pointers bar is taller than left here
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    res += leftmax - height[left]
                left += 1

            else:  # here left is taller than right so do the right pointer manipulations
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    res += rightmax - height[right]

                right -= 1

        return res

