# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Recursive solution O(N) and O(Height of binary tree) i.e. (O(LOGN) in average case)
class Solution(object):
    def __init__(self):
        self.answer = None  #set a  global variable or class variable for storing answer 
    
    def lowestCommonAncestor(self, root, p, q):
        
        def lca(node):
            if node is None:
                return False

            left = lca(node.left) #this will keep on recursing until one or both are found and 
            right = lca(node.right)

            mid  = False
            if (node == p or node == q):
                mid = True #set to True or 1 if either found

            if mid + left + right >=2: #if "any two of it is true" then the current node is LCA
                self.answer = node
                return True #optional

            return mid or left or right #can also be "return mid+left+right >0"

        lca(root)
        return self.answer