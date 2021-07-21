class Solution(object):
    "abccb"
    # limit check is here
    #O(N^2) time and O(1) space most optimal

    #aabbaa
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            # expand odd palindrome
            count += self.countByExpand(s, i, i)

            # expand even palindrome
            count += self.countByExpand(s, i, i + 1)

        return count

    #expanding around the centre for each element in the array
    def countByExpand(self, string, left, right):
        count = 0
        while left >= 0 and right < len(string):
            if string[left] != string[right]: #not a palindrome if this happens so break
                break
            count += 1

            left -= 1
            right += 1

        return count