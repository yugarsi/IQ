'''
Approach 4: Expand Around Center
In fact, we could solve it in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and there are only 2n−1 such centers.

'''

#O(N^2) and O(1) space
#Find longest palindrome substring


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0

        sindex = 0
        eindex = 0
        for i in range(len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i, i + 1)

            curlen = max(odd, even)
            if curlen > longest:
                longest = curlen
                sindex = i - (longest - 1) / 2
                eindex = i + longest / 2

        return s[sindex:eindex + 1]

    #expands and returns the length of the longest palindromic substring
    def expandAroundCenter(self, string, left, right):

        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left -= 1
            right += 1

        return right - left - 1 #remember length is -1 not +1
