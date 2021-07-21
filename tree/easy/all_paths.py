# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getPaths(self, node, curr, paths):
        if node:
            curr += str(node.val)
            if node.left is None and node.right is None:
                paths.append(curr)
            else:
                curr += "->" 
                self.getPaths(node.left, curr, paths)
                self.getPaths(node.right, curr, paths)
        
        
    def binaryTreePaths(self, root):
        cur = ""
        op = []
        self.getPaths(root, cur, op)
        return op