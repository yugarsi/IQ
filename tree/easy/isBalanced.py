# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_NLOGN_TIME: #O(NLOGN) or O(N^2) solution
    #TOP down recursion unneccesary  height computation at each step
    def height(self, node):
        if node is None:
            return 0
        leftdepth = self.height(node.left)
        rightdepth = self.height(node.right)
        return 1 + max(leftdepth,rightdepth)

    def isBalanced(self, root):
        if root is None:
            return True
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return abs(leftHeight - rightHeight) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

###BEST SOLUTION
class Solution:
    #Simpler method return earlier if not balanced.. have two different type of response
    #-1 for not balanced or not post_order bottom up recursion
    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if (lh == -1 or rh == -1 or abs(lh-rh) > 1):
            return -1
        return 1 + max(lh,rh)
    
    def isBalanced(self, root):
        height = self.height(root)
        return height != -1

#Leetcode solution
class Solution:
    #Bottom up recursion in O(N)
    #basically computes depth and balance state within at the time
    def helper(self, root):
        if root is None:
            return 0, True
        lh , lb = self.helper(root.left)
        if not lb:
            return 0, False
        rh, rb = self.helper(root.right)
        if not rb:
            return  0, False
        
        #returns height and balanced state together
        return 1+max(lh, rh), (abs(lh-rh) < 2)
        
        
    def isBalanced(self, root):
        height , bal = self.helper(root)
        return bal
        