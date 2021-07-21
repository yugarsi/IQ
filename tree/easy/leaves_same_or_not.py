# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLeafNodes(self, root, leaves):
        if root is None:
            return
        if (root.left is None and root.right is None):
            leaves.append(root.val)
        
        self.getLeafNodes(root.left, leaves)
        self.getLeafNodes(root.right, leaves)
        
        
    def leafSimilar(self, root1, root2):
        t1 = []
        t2 = []
        self.getLeafNodes(root1, t1)
        self.getLeafNodes(root2, t2)
        return t1 == t2