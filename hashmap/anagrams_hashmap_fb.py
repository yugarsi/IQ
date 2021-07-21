class Solution:
    #O(N+P) time and O(1) max 26 elements
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls , lp = len(s),len(p)
        if ls<lp:
            return []
        
        phash = {}
        for i in range(lp):
            if p[i] in phash:
                phash[p[i]] += 1
            else:
                phash[p[i]] = 1
                
        shash = {}
        res = []
        for i in range(ls):
            if s[i] in shash:
                shash[s[i]] += 1
            else:
                shash[s[i]] = 1
            if i >= lp:
                if shash[s[i-lp]] == 1:
                    del shash[s[i-lp]]
                else:
                    shash[s[i-lp]] -= 1
                    
            if shash == phash:
                res.append(i-lp+1)
        return res

#Using counter which is a hashmap as well
class Solution(object):
    def findAnagrams(self, s, p):
        ls,lp = len(s),len(p)
        if lp > ls:
            return []
        
        anagrams = []
        pcount = collections.Counter(p)
        scount = collections.Counter()
        for i in range(ls):
            scount[s[i]] += 1
            if i >= lp:
                
                if scount[s[i-lp]] == 1:
                    del(scount[s[i-lp]])
                else:
                    scount[s[i-lp]] -= 1
            if pcount == scount:
                anagrams.append(i-lp+1)
        return anagrams