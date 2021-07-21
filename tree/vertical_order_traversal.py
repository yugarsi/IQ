#NOTE there is NO equivalent of TreeMap (sorted keys dictionary) in Python
#There is collections.OrderedDict which stores keys in the order which elements were added to the dict
#>>> a = OrderedDict()
# >>> a[4] = 1
# >>> a
# OrderedDict([(4, 1)])
# >>> a[6] = 2
# >>> print(a.keys())
# [4, 6]
# >>> print(a.values())
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        hashmap = collections.defaultdict(list) #map --> column_no : [list of nodes]
        
        queue = []
        if root is None:
            return []
        queue.append((root,0)) #Adding root's level = 0
        minlevel = 0 #for avoiding sorting the hashmap #can use treemap in java
        maxlevel = 0
        while queue:
            curLen = len(queue)
            for i in range(curLen):
                cur,level = queue.pop(0)
                if level < minlevel:
                    minlevel = level
                if level > maxlevel:
                    maxlevel = level
                hashmap[level].append(cur.val)
                if cur.left:
                    queue.append((cur.left, level-1))
                if cur.right:
                    queue.append((cur.right, level+1))
        
        res = []
        for i in range(minlevel,maxlevel+1):
            if i in hashmap:
                res.append(hashmap[i])
        return res
        
    