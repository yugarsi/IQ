"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    #connect left to right in Tree
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root is None:
            return None
        queue.append(root)  #level order traversal
        while queue:
            curLen = len(queue)
            for i in range(curLen):  # iterate level by level
                cur = queue.pop(0)
                if (i < curLen-1):
                    cur.next = queue[0] #it pops the top and then next queue[0] is the next item
                    
                else:
                    cur.next = None #not needed
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
        return root
        