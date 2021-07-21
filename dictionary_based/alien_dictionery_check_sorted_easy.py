'''
In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.
'''
class Solution:

    # abcde #abc
    def checkOrder(self, s1, s2, omap):  # returns True if s1 is before s2

        i = 0
        while i < len(s1) and i < len(s2):
            if omap[s1[i]] > omap[s2[i]]:
                return False
            elif omap[s1[i]] < omap[s2[i]]:
                return True
            # only if both orders are equal we have to iterate till the end
            i += 1

        return len(s1) <= len(s2)

    def isAlienSorted(self, words, order: str) -> bool:
        omap = {}
        i = 0
        for c in order:
            omap[c] = i
            i += 1

        for j in range(1, len(words)):  # compare consecutive words
            if not self.checkOrder(words[j - 1], words[j], omap):
                return False

        return True
