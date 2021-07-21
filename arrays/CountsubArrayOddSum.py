class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cursum = 0
        oddsubcount = 0
        odd = 0
        even = 1
        for i in range(len(arr)):
            cursum = (cursum + arr[i])%2
            if (cursum % 2 == 0):
                oddsubcount = (oddsubcount + odd)%1000000007
                even += 1
            else:
                oddsubcount = (oddsubcount + even)%1000000007
                odd += 1
        
        return oddsubcount
            
        