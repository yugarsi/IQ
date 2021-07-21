class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        queue = []
        queue.append(root)
        level = 0
        res = []
        while queue:
            curlen = len(queue)
            levelRes = []  #inner each level result double linked list
            for i in range(curlen):  #this is another way of doing BFS knowing how many nodes in each level by len(queue)
                cur = queue.pop(0)
                if level % 2 != 0:
                    levelRes.insert(0, cur.val)
                else:
                    levelRes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
            res.append(levelRes)
        
        return res