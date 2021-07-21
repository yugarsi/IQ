# Definition for a binary tree node.
# Range SUM in BST
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def rangeSumBST(self, root, low, high):
        self.s = 0

        def DFS(root, s):
            if root is None:
                return
            if root.val >= low and root.val <= high:
                self.s += root.val
            if root.val >= low:
                DFS(root.left, s)
            if root.val <= high:
                DFS(root.right, s)

        DFS(root, 0)
        return self.s
