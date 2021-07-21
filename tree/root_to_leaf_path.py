class Solution1(object):
    def getPaths(self, node, curr, paths):
        if node:
            curr += str(node.val)
            if node.left is None and node.right is None:
                paths.append(curr)
            else:
                curr += "->" 
                self.getPaths(node.left, curr, paths)
                self.getPaths(node.right, curr, paths)
        
        
    def binaryTreePaths(self, root):
        cur = ""
        op = []
        self.getPaths(root, cur, op)
        return op

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths
        