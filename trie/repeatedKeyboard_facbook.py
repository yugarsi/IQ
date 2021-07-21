class Trie:
    def __init__(self):
        self.word=None
        self.children = {}
        self.isEnd = False

def insert(root, word):
    temp = root
    for w in word:
        if w not in temp.children:
            temp.children[w] = Trie()
        temp = temp.children[w]

    temp.word = word #save the word itself in the end
    temp.isEnd = True

#abc
#aabcc
def isMatch(node, query):
    if node.isEnd and query == "": #base case
        return (True , node.word)
    if query == "":
        return (False , None)
    first, remaining = query[0], query[1:]

    if first in node.children:
        stat1 , w1 = isMatch(node.children[first], remaining)
        stat2, w2 = False,None
        if remaining != "" and remaining[0] == first:
            stat2, w2 =  isMatch(node.children[first], remaining[1:])
        w = w1 if stat1 else w2
        if stat1 or stat2:
            return (True, w)

    return (False, None)
words = [ "booy", "girl", "mann"]
root = Trie()
for word in words:
    insert(root, word)

#booy
#booooy
#you have to see if query in dictionary and return the word it matches
print( isMatch(root, "booy"))
print( isMatch(root, "booooyy"))
print( isMatch(root, "mannnn"))
print( isMatch(root, "mannnnn"))