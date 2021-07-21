"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

#BFS approach
from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):

    #Using DFS
    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        visited = {}
        
        def dfs(node):
            if node is None:
                return node
            if node in visited:
                return visited[node]
                #visited will contain key = graph1 node and value = graph 2's node
            
            clone = Node(node.val)
            visited[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        return dfs(node)

    #Using BFS
    def cloneGraph(self, node):

        if not node:
            return node

        visited = {}

        queue = deque([node])
        visited[node] = Node(node.val, []). 
        #visited will contain key = graph1 node and value = graph 2's node

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]