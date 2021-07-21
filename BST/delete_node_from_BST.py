class Solution:
    
    def getsuccessor(self, node):
        node = node.right
        while node.left:
            node=node.left
        return node.val
    
    def getpred(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
    
    #deleting and returning root itself 
    #Remember!! so each call returns whichever node we are calling

    #O(logN) in case of balaced tree O(H) space
    def deleteNode(self, root, key):
        
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key) #Logn if balanced
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else: #found element here
            
            if root.left is None and root.right is None: #leaf node so just delete it.
                root = None
            
            elif root.right:
                root.val = self.getsuccessor(root)  #get successor and then recursively delete that node
                root.right = self.deleteNode(root.right, root.val) #delete successor
                
            else:
                root.val = self.getpred(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root
                