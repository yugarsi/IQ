
class Solution:
    #checks if two trees are identical
    def isIdentical(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False

        left = self.isIdentical(n1.left , n2.left) 
        right = self.isIdentical(n1.right , n2.right)
        
        if left and right and n1.val == n2.val:
            return True
        else:
            return False
    
    #Check for each node()
    def isSubtree(self, root: TreeNode, subroot: TreeNode) -> bool:
        
        if root is None:
            return False
        
        if root.val == subroot.val:
            if self.isIdentical(root, subroot):
                return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
        
        
        