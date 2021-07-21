from collections import defaultdict

'''
Alien dictionary order
three steps.

1. Extracting dependency rules from the input. For example "A must be before C", "X must be before D", 
or "E must be before B".
2. Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
3. Topologically sorting the graph nodes.
'''


class Solution:

    # with one word order can't be derived so derive order from two words and put it in graph
    # each node graph contains a character and the edge represents the next character (it is a directed graph)
    def deriveOrder(self, word1, word2, graph, indegree):
        n = min(len(word1), len(word2))
        for i in range(n):
            if word1[i] != word2[i]:
                curr = graph[word1[i]]
                if word2[i] not in curr:  # this is needed for sake of indegree
                    curr.add(word2[i])
                    indegree[word2[i]] += 1  # increment in degree
                break

    def alienOrder(self, words):
        # hashmap of set (adjacency list representation)
        graph = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0
                graph[c] = set()  # optional as default dict initializes anyway

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # if helloworld before hello => wrong order
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            self.deriveOrder(word1, word2, graph, indegree)

        output = []
        queue = []

        # TOPOLOGICAL SORT LOGIC
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)

        while queue != []:
            curr = queue.pop(0)
            output.append(curr)
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        # if all alphabets/chars not covered return none
        if len(output) < len(indegree):
            return ""

        return "".join(output)