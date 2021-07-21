'''
846. Hand of Straights

Share
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size groupSize, and consists of groupSize consecutive cards.

Return true if and only if she can.

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if it is possible. Otherwise, return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
'''

class Solution(object):
    def isPossibleDivide(self, nums, k):
        fre = Counter(nums)
        # greedy solution, take the smallest then try
        vals = list(fre.keys())
        heapq.heapify(vals)

        # every iteration i make a new list
        while len(vals):
            # let us start with the minimum element
            start = vals[0]
            # now create a list starting with 'start'
            for i in range(k):
                if fre[start + i]:
                    fre[start + i] -= 1
                else:
                    return False
            # pop any elements which are not remaining
            while len(vals) and fre[vals[0]] == 0:
                heapq.heappop(vals)

        return True
