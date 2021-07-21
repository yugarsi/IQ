'''
There are several other data structures, like balanced trees and hash tables, 
which give us the possibility to binary_search for a word in a dataset of strings.
Then why do we need trie? Although hash table has O(1) time complexity for looking for a key,
 it is not efficient in the following operations :

1. Finding all keys with a common prefix.
2. Enumerating a dataset of strings in lexicographical order.

Another reason why trie outperforms hash table, is 
that as hash table increases in size, there are lots of hash collisions and the binary_search time complexity
could deteriorate to O(n), where n is the number of keys inserted. 
Trie could use less space compared to Hash Table when storing many keys with the same prefix. 
In this case using trie has only O(m) time complexity, where m is the key length.
 Searching for a key in a balanced tree costs O(mlogn) time complexity.

 '''
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        temp = self.trie
        for w in word:
            if w in temp:
                temp=temp[w]
            else:
                temp[w]={}
                temp=temp[w]
        temp['#'] = True
        print(self.trie)
        print (temp)


    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        temp = self.trie
        for w in word:
            if w in temp:
                temp = temp[w]
            else:
                return False
        return '#' in temp



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.trie
        for w in prefix:
            if w in temp:
                temp = temp[w]
            else:
                return False
        return True

tr = Trie()
tr.insert("abc")
tr.insert("cde")