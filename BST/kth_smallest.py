#Time complexity(O(H + k))
class Solution(object):
    def kthSmallest(self, root, k):
        if root is None:
            return None
        
        stack = []
        stack.append(root)
        
        #assumption that k is smaller than N
        #Outer loop
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k==0:
                return root.val #this breaks the outer loop
            root = root.right