class Solution:
    def rightSideView(self, root):
        #level order and print the rightmost
        queue = []
        output = []
        if root is None:
            return []
        
        queue.append(root)
        while queue:
            levellen = len(queue)
            output.append(queue[-1].val)
            for i in range(levellen):
                cur = queue.pop(0)
                if (cur.left):
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return output

    # Using recursion, i.e. DFS
    class Solution:
        def rightSideView(self, root):

            if root is None:
                return []

            res = []

            def DFS(node, level):
                if node is None:
                    return
                if len(res) == level:
                    res.append(node.val)

                if node.right:
                    DFS(node.right, level + 1)
                if node.left:
                    DFS(node.left, level + 1)

            DFS(root, 0)
            return res
