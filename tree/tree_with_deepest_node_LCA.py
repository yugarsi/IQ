# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The most important points is, BFS starts visiting nodes from root 
#while DFS starts visiting nodes from LEAF. (IN ORDER and PRE ORDER)
# So if our problem is to binary_search something that is more likely to closer to root, we would prefer BFS.
# And if the target node is close to a leaf, we would prefer DFS.
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        depth = {None : -1}
        def dfs(node, parent = None):
            if node == None:
                return
            else:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root) #finds depth of all nodes and saves in hashmap
        maxdepth = max(depth.itervalues()) #max depth in hashmap
        def lca(node):
            if not node or depth[node] == maxdepth:
                return node
            left = lca(node.left)
            right = lca(node.right)
            
            if left is not None and right is not None:
                return node
            if left is not None:
                return left
            if right is not None:
                return right
            return None
        
        return lca(root)