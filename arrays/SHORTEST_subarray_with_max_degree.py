class Solution(object):

    '''
    find shortest sub-array with degree same as original array.

    Degree =maximum frequency of any character/number
    '''
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countmap = {}
        left = {}  # maintain the left occurence of any character
        right = {} #maintain index of rightmost occurence of any character

        for i, n in enumerate(nums):
            if n not in left:
                left[n] = i  # this will be leftmost occurence

            right[n] = i  # this will be the rightmost occurence
            if n in countmap:
                countmap[n] += 1
            else:
                countmap[n] = 1

        degree = max(countmap.values())
        ans = len(nums)
        for x in countmap:
            if countmap[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans