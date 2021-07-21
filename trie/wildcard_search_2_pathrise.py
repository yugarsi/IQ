class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False


#recursive insertion
def insert(word, trieNode):
    if word == "":
        trieNode.isLeaf = True
        return
    first , remain = word[0], word[1:]
    if first in trieNode.children:
        insert(remain, trieNode.children[first])
    else: #this else can be ignored if you return after insert
        node = TrieNode(first)
        trieNode.children[first] = node
        insert(remain, node)

#recursive binary_search
def search(query, trieNode):
    if query == "" and trieNode.isLeaf:
        return True
    if query == "":
        return False
    first, remain = query[0],query[1:]
    if first == ".":
        for n in trieNode.children:
            return search(remain, trieNode.children[n])

    elif first in trieNode.children:
        return search(remain, trieNode.children[first])

    return False


words = ["foobar", "foo", "foos", "food"]
trie = TrieNode("")
for w in words:
    insert(w, trie)

query = "foob.r"

print (search(query, trie))
