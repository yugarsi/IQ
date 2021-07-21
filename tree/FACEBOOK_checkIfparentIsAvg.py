def checkIfavg(node):
    if node is None:
        return True

    left,right = node.left,node.right

    if left is None and right is None:
        return True

    if left and right:
        avg = (left.val + right.val) // 2
    elif right is None:
        avg = left.val
    elif left is None:
        avg = right.val

    if node.val == avg and checkIfavg(node.left) and checkIfavg(node.right):
        return True
    else:
        return False