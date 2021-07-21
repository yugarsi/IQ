class Solution:
    def isCousinsBrutForce(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        info = {root.val: (-1, 0)}
        
        def getLevels(node, info):
            if node:
                parent,depth = info[node.val]
                if node.left:
                    info[node.left.val] = (node.val, depth+1)
                    getLevels(node.left, info)
                if node.right:
                    info[node.right.val] = (node.val, depth+1)
                    getLevels(node.right, info)
        
        getLevels(root, info)

        px, dx = info[x]
        py, dy = info[y]
        
        if dx == dy and px != py:
            return True
        else:
            return False
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        xparent = -1
        yparent = -2
        xdepth = -1
        ydepth = -2
        
        if root is None:
            return False
        queue = []
        queue.append((-1, root))
        
        level = 0
        xfound = False
        yfound = False
        while queue != []:
            for i in range(len(queue)):
                curr = queue.pop(0)
                parent = curr[0]
                node = curr[1]
                
                if node.val == x:
                    xdepth = level
                    xparent = parent
                    xfound = True
                if node.val == y:
                    ydepth = level
                    yparent = parent
                    yfound = True
                
                if node.left:
                    queue.append((node.val,node.left))
                if node.right:
                    queue.append((node.val, node.right))
            
            if xfound and yfound:
                return xdepth == ydepth and xparent != yparent
            level += 1
        
        return False