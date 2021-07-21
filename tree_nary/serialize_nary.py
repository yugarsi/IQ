class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []
#ALGORITHM is to add length of each children into the serialized string to be used later for deserialization
def rserialize(node, res = []):
    if node is None:
        return
    res.append(str(node.val))
    chlen = len(node.children)
    res.append(str(chlen))
    for child in node.children:
        rserialize(child, res)

counter = 0
def rdeserialize(slist):
    global counter #updating the global variable to keep track of how many nodes processed
    if counter == len(slist):
        return
    nodeval = slist[counter]
    counter += 1
    node = Tree(int(nodeval))
    chlen = int(slist[counter])
    for i in range(chlen):
        counter += 1 #remember to increment for each children INSIDE THE LOOP
        node.children.append(rdeserialize(slist))
    return node


root = Tree(1)
ch1= [Tree(2), Tree(3), Tree(4)]
ch1_1 = [Tree(5), Tree(6)]
root.children = ch1
root.children[0].children = ch1_1


sbuilder = []
rserialize(root, sbuilder)
print(sbuilder)
newroot = rdeserialize(sbuilder)

# print (newroot.val)
# print (newroot.children)
newbuilder = []
rserialize(newroot, newbuilder)
print(newbuilder)





