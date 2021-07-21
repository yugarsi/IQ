'''
Your friend is typing his name into a keyboard. Sometimes,
when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # llleelee #lllleeelee
        i = 0
        j = 0
        while j < len(typed): #iterate for longer string

            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1

            else:
                if j > 0 and typed[j] == typed[j - 1]: #if extra pressed
                    j += 1
                else: #this indicates different char
                    return False

        return i == len(name) #all chars should be covered #check for none if 

