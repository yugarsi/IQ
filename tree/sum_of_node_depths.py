#using iterative BFS (level order traversal)
#find sum of node depths

def nodeDepths(root):
	if root is None:
		return 0
    queue = []
	dsum = 0
	queue.append(root)
	level = 0
	while queue != []:
		qlen = len(queue)
		for i in range(qlen):
			cur = queue.pop(0)
			dsum += level
			if cur.left:
				queue.append(cur.left)
			if cur.right:
				queue.append(cur.right)
		level += 1
	
	return dsum