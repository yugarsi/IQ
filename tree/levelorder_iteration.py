from collections import deque
class Solution:
    def levelOrder(self, root):

        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            level_length = len(queue)            
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return levels