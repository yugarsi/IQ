
def lengthOfLongestSubstring(self, s):
    left = 0
    maxLen = 0
    maxSubstring = ""
    indexMap = {}              
    for right in range(len(s)):
        curr = s[right]
        if curr in indexMap:                      # if you don't add the indexmap[cur] + 1 here add in line 18
            left = max(left, indexMap[curr]+1)   #"example - abcb, left =0 and indexmap[cur] = 1 so move to location c i.e. indexmap[cur] + 1 "
            
        newMax = max(maxLen, right-left+1)
        if newMax > maxLen:                    #this part only only needed if we need to 
                                              #finf the substring
            maxSubstring = s[left: right+1]   #not needed for just length
            maxLen = newMax                   #not needed for just length
            
        indexMap[curr] = right #add here if 
    
    print (maxSubstring)
    return maxLen


#using sliding window
def lengthOfLongestSubstring(self, s):
    charlist = [0] * 128
    left = right = 0 ##initialize two pointers
    
    maxlen = 0
    for right in range(len(s)):
        cur = s[right]
        charlist[ord(cur)] += 1
        
        while charlist[ord(cur)] > 1:      
            charlist[ord(s[left])] -= 1   #remove the previous elements from window until the occurence of s[right] is removed
            left += 1                      #increment left side of window
        maxlen = max(maxlen, right-left+1)
    
    return maxlen
                