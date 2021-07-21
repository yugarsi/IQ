
###Very important to do post order left_sum + right_sum + node.val
#but modify tilt globally
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt

            if not node:
                return 0

            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return left_sum + right_sum + node.val

        valueSum(root)

        return total_tilt


#PYthon 2 solution as nonlocal not supported using a hashmap
class Solution(object):
        
    def findTilt(self, root):
        globalsum = {"t":0}
        def findTiltSum(node):
            if node is None:
                return 0
            leftsum = findTiltSum(node.left)
            rightsum = findTiltSum(node.right)
            globalsum["t"] += abs(leftsum-rightsum)
        
            return node.val + leftsum + rightsum
        
        findTiltSum(root)
        return globalsum["t"]