# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxlen = 0. #global variable to track max path len (through the root)
        def getDiameter(node, pathlen=0):  #recursively get height
            nonlocal maxlen
            if node is None:
                return 0

            #post order traversal 
            leftlen = getDiameter(node.left, pathlen) #this returns maxlen/height in left sub tree 
            rightlen = getDiameter(node.right, pathlen) #this returns maxlen/height in left sub tree 
            
            curlen = leftlen + rightlen #find left+right path and save in global variable
            if curlen > maxlen:
                maxlen = curlen
            
            return 1 + max(leftlen, rightlen) #return height 
        
        getDiameter(root)
        return maxlen