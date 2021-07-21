#given two strings return true if the string is only one distance away

#Time complexity : O(N) in the worst case when string lengths are close enough 
#abs(ns - nt) <= 1, where N is a number of characters in the longest string. 
#O(1) in the best case when abs(ns - nt) > 1.

#Space complexity = O(N) because strings are immutable in Python and Java 
#and to create substring costs \mathcal{O}(N)O(N) space.
class Solution:
    def isOneEditDistance(self, s, t):
        #solving with s smaller than t
        lens,lent = len(s),len(t)
        if lens > lent:
            return self.isOneEditDistance(t,s) #to ensure s is always smaller than t
            
        if (lent - lens) > 1:
            return False

        for i in range (lens):  #O(N)
            if s[i] != t[i]:  #only then there is a chance of diff
                
                if (s[i+1:] == t[i+1:]): #case where the strings are of equal length 
                                        #you are just creating substring only one time hence O(1)
                    return True
                
                elif (s[i:] == t[i+1:]):
                    return True
                else:
                    return False
        
        return  lens+1 == lent
    
        