#1,2,None,None,3,4,None,None,5,None,None,
# In this task, however, the DFS strategy is more adapted for our needs, 
# since the linkage among the adjacent nodes is naturally encoded in the order,
# which is rather helpful for the later task of deserialization.



class Codec:

	#O(N) time and space O(N) for both
	#serializes based on pre-order traversal of nodes 
	#If Nones are appended then you can determine any signature by preorder itself
    def serialize(self, root):
        def rserialize(root , nodes = []): #passing an array where we put values
            if root is None:
                nodes.append ("None")
                return
            nodes.append(str(root.val))
            rserialize(root.left , nodes)
            rserialize(root.right, nodes)
        
        nodes = []
        rserialize(root, nodes)
        return (",".join(nodes)) #then join the values #Like string builder more efficient than "+"
            
                
    def deserialize(self, data):
        
        #treats like a queue and pops everything from front of 
        #list/queue and goes on to create a tree 
        #Node list.pop(0) throws exception when empty 
        #can use queue = collections.deque() queue.append([node]), queue.popleft()
        def rdeserial(nodes):
            cur = nodes.pop(0)
            if cur == "None":
                return None
            
            curNode = TreeNode(int(cur))
            curNode.left = rdeserial(nodes)
            curNode.right = rdeserial(nodes)
            return curNode
        
        nodes = data.split(",")
        return rdeserial(nodes)
       