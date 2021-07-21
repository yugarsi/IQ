# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    #O(N) additional memory (for storing in a list) and O(1)
    def __init__(self, root):
        self.arr = self.inorder(root)
        self.cur = 0
        self.max = len(self.arr)
    
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
    
    def next(self):
        if self.cur < self.max:
            val = self.arr[self.cur]
            self.cur += 1
            return val
        else:
            return None
    def hasNext(self):
        return self.cur < self.max


#Controlled recursion Avg O(1) has next() and O(h) extra space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.leftStack(root)
        

    def leftStack(self, node):  #keep appending all left elements in a stack and therefore smallest in top
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self): #pop smallest then put right in stack using leftstack()
        cur = self.stack.pop()
        if cur.right:
            self.leftStack(cur.right)
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0 #returns true if len(stack) > 0