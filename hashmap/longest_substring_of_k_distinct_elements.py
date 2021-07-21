class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        distinct = {} #hashmap of distinct elements O(k) space complexity and O(N) time complexity 
                      #100% best answer
        
        i=0
        j=0
        
        maxlen = 0
        for j in range(len(s)):
            
            if s[j] in distinct:    #if in distinct then increment
                distinct[s[j]] += 1
            else:
                distinct[s[j]] = 1
            
            setsize = len(distinct) 
            if setsize <= k:        #if hashmapsize <= k then keep checking curlen = j-i+1 
                curlen = j-i+1
                if curlen>maxlen:
                    maxlen = curlen
            
            else:                    #else update the hashmap
                distinct[s[i]] -= 1
                if distinct[s[i]] == 0:
                    del (distinct[s[i]])
                i += 1
        
        return maxlen
            
        