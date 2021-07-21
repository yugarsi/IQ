
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Codec:
    indexCount = 0
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList)
        return ",".join(serializedList)
    
    def _serializeHelper(self, root, serializedList):
        if not root:
            return
        
        # Actual value
        serializedList.append(str(root.val))
        
        # Number of children
        chlen = len(root.children) #assumption children is empty list
        serializedList.append(str(chlen))

        for child in root.children:
            self._serializeHelper(child, serializedList)
    
    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data:
            return None
        
        self.indexCount = 0 #index is number of string nodes processed
        return self._deserializeHelper(data.split(","))
        
    def _deserializeHelper(self, data):
        
        if self.indexCount == len(data): #if all data processed return
            return None
        
        val = data[self.indexCount]
        node = Node(int(val), [])
        self.indexCount +=1
        numChildren = int(data[self.indexCount])
        for i in range(numChildren):
            self.indexCount +=1   #remember to increment for each children INSIDE THE LOOP
            node.children.append(self._deserializeHelper(data))
        return node    