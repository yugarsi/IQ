#INORDER AND PREORDER/POSTORDER uniquely identify a binary tree

class Solution(object):
    #postorder iterative (this is just reversing the output or if output is a stack it works)
    def postorderTraversal(self, root):
        stack  = []
        output = []
        if root == None:
            return []
        stack.append(root)
        while stack != []:
            cur = stack.pop()
            output.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return reversed(output)



    # inorder iterative
    def inorderTraversal(self, root):
        output = []
        stack = []
        if root is None:
            return []
        
        cur = root
        while  cur or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            output.append(cur.val)
            cur = cur.right
            
        
        return output

    #preorder iterative
    def preorderTraversal(self, root):
        stack = []
        output = []
        cur = root
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node is not None:
                output.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                
        return output



    def postorderTraversal(self, root):
        if (root ==None):
            return []
        res = self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        return res + [root.val]
    
#     I was looking for a proper iterative solution where we use a stack only by adding elements to the top of it, since it feels like cheating (and insert(0, ) might lead to quadratic time complexity...)
# Wikipedia has a section about this, so I adopted a bit the code for something one would show in an interview.
# Taken from https://en.wikipedia.org/wiki/Tree_traversal#Post-order

# For this we need a stack and a variable last_visited to account for the last node where we have done some operation (in this case append to the output list)

# Like in the in-order tree traversal, append all left children of the nodes to the stack. Peek would be the leftmost child of the current 'tree' (the element in the top of the stack)
# a) If the leftmost has a right child that we haven't visited already, we explore it (node = peek.right) and do step 1)
# b) If the leftmost node has no right child or we have visited it already, we pop it (visit it) and thus can repeat a) or b) accordingly with the next element in the stack (peek again)

    #in order to return output in right order
    def postorderTraversalIter(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        last_visited = None
        while stack or node:
            # Add leftmost node to the stack first
            while node:
                stack.append(node)
                node = node.left
            peek = stack[-1]

            # Append to answer if we visited already right side of top of the stack
            if peek.right is None or peek.right == last_visited:
                last_visited = stack.pop()
                res.append(last_visited.val)
            # Visit right side
            else:
                node = peek.right

        return res
        

