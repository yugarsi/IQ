# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm (using postorder traversal)
# 1. recursivele first flatten left sub tree and right subtree
# left recursive call returns lefttail
# right recursive call return righttail
# 2. Then after that => if lefttail exisits, lefttail.right= node.right
# 3. node.right = node.left (flatten)
# 4. node.left = None
# then return righttail if it exists else return lefttail
# O(N) time and O(N) Space
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return node
            lefttail = flat(node.left)  # postorder first flatten left and right and get end element
            righttail = flat(node.right)  # postorder flatten right

            if lefttail:
                lefttail.right = node.right  # put right in lefttail
                node.right = node.left  # put left in right
                node.left = None  # left becomes None

            if righttail:
                return righttail
            else:
                return lefttail
        flat(root)