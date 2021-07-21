class Trie:
    def __init__(self):
        self.key = None
        self.chars = [None]*26

def insert(trie, word):  #max depth is 26
    cur = trie
    for w in word:
        key = ord(w) - ord('a')   #each level is for english alphabets in order a = 0 to z=25
        if cur.chars[key] is None:
            cur.chars[key] = Trie()
        cur = cur.chars[key]

    cur.key = word #store the word Itself as a key in the leaf

def preOrder(trie, words):
    if trie is None:
        return

    for i in range(26):
        if trie.chars[i]:
            if trie.chars[i].key: #if leaf node append to results
                words.append(trie.chars[i].key)
            preOrder(trie.chars[i], words)


words = ["abd", "acg", "aa", "a", "bce", "zz", "aab"]

trie = Trie()
for word in words:
    insert(trie, word)

res = []
preOrder(trie, res)
print (res)
