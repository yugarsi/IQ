class Solution:
    def reverseWords(self, s):
        words = s.split()
        return " ".join([ele for ele in reversed(words)])

#own Solution for reverse

class Solution:
    def reverse(self, arr):
        left = 0
        right = len(arr) - 1
        while(left < right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        return arr
    
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(self.reverse(words))
