trie = {}

"foobar"
#{ "f" : {"o":{"o":{ "b": {"a":{"r":{"#":-1}}}} }}}
def insertWordInTrie(word):
    temp = trie
    for w in word:
        if w not in temp:
            temp[w] = {}
        temp = temp[w]
    temp["#"] = -1


def search(query , trienode):
    if query == "" and "#" in trienode:
        return True
    if query == "":
        return False
    first, remaining = query[0], query[1:]
    print (first, remaining)
    print (trienode)
    if first == ".":
        for element in trienode:
            if element!= "#":
                return search(remaining, trienode[element])
    elif first in trienode:
        return search(remaining, trienode[first])
    return False

words = ["foobar", "foo", "foos", "food"]
for w in words:
    insertWordInTrie(w)

query = "foobar"
print (search(query, trie))
