
class Trie:
    def __init__(self):
        self.word = None
        self.children = {}
        self.isEnd = False

def insert(root, dir):
    temp = root
    for char in dir:
        if char not in temp.children:
            temp.children[char] = Trie()
        temp = temp.children[char]

    temp.isEnd = True
    temp.word = dir

def removeRedundant(root, dir):
    temp = root
    for char in dir:
        if temp.isEnd:
            return temp.word
        temp = temp.children[char]

    return temp.word

root = Trie()

dirs = ["/abc/b/a", "/abc/b", "/abc/c","/abc/d", "/bcd", "/cde"]
for dir in dirs:
    insert(root, dir)

res = set()
for dir in dirs:
    newD = removeRedundant(root, dir)
    res.add(newD)

print (list(res))
#even the split operation will be o(m * n) where n is the number of dirs, m is the length ogf each dir
print ("/bac/".split("/"))