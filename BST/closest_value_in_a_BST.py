#One approach is recursive inorder traversal create array and then binary_search closest
#O(N) = time  and O(N) = space for array

#Iterative approach using binary binary_search as then we can find in O(H) height of tree
#i.e. (log(N) avg time) and O(1) space
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        mindiff = float("inf")
        cval = root.val
        curr = root
        while curr:
            diff = abs(target - curr.val)
            if diff < mindiff:
                mindiff = diff
                cval = curr.val
            
            if curr.val < target:
                curr = curr.right
            elif curr.val > target:
                curr = curr.left
            else:
                return curr.val
        
        return cval
        