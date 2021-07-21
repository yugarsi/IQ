# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Binary Tree average of levels
class Solution:

    #Average of levels by BFS i.e. level order traversal
    def averageOfLevels(self, root):
        avgs = []
        if root is None:
            return avgs
        
        queue = []
        queue.append(root)
        while queue != []:
            lsum = 0
            levelLen = len(queue)
            for i in range(levelLen):
                cur = queue.pop(0)
                lsum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            avgs.append(lsum/levelLen)
        return avgs

    #brute force algo find levels of each node and store in hash map
    def averageOfLevelsOwnAlgo(self, root):
        #dfs find depth of each level
        depth = {None: -1}
        
        def findDepth(node, parent=None):
            if node == None:
                return
            else:
                depth[node] = depth[parent]+1
            
            findDepth(node.left, node)
            findDepth(node.right, node)
        
        findDepth(root)
        
        maxdepth = max(depth.values())
        
        levelsum = [0] * (maxdepth+1)
        count = [0]* (maxdepth+1)
        
        for d in depth:
            level = depth[d]
            if level >= 0:
                levelsum[level] += d.val
                count[level] += 1
        
        output = []
        for i in range(maxdepth+1):
            output.append(levelsum[i]/count[i])
        
        return output    
    
    