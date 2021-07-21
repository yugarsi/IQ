class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchsum(root, bsum, sums):
	if root is None:
		return
	bsum = bsum + root.value
	if root.left is None and root.right is None:
		sums.append(bsum)
	branchsum(root.left, bsum, sums)
	branchsum(root.right, bsum, sums)
	
	
def branchSums(root):
	sums = []
    branchsum(root, 0, sums)
	return sums
