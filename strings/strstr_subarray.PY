class Solution:
    def strStr(self, h: str, n: str) -> int:
        if n == "":
            return 0
        j = 0
        i = 0
        while i < len(h):
            if h[i] == n[j]:
                i+=1
                j+=1
                if j == len(n):
                    return i-j
            
            else:
                i = i - j + 1
                j = 0
            
        return -1
            