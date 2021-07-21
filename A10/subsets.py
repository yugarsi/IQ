def get_all_subsets(arr):
    n = len(arr)
    res = []
    for i in range(0, pow(2,n)):
        subset = []
        for j in range(0, len(arr)):
            if( i & (1 << j)) > 0:
                subset.append(arr[j])
        res.append(subset)
    return res

arr = [1,2,2]
#[[], [1], [1,2], [1,2,2], [2], [2,2]]

#arr = [1,2,3,4]
print (get_all_subsets(arr))

from collections import deque
def getsubsetsBFS(nums):
    queue = deque([[]])
    i = 0
    while queue and i<len(nums):
        N = len(queue)
        for j in range(N):
            lst = queue.popleft()
            prev = None
            if len(queue) > 0:
                prev = queue[-1]
            if lst[:] != prev:
                queue.append(lst[:])
            if prev != lst + [nums[i]]:
                queue.append(lst + [nums[i]])
        i += 1
    return list(queue)

# [1,2,2]
# []
# [] [1]  #look ahead and see if it's the same
# [][1][2][1,2]
# [][1][2][2,2] [1,2][1,2,2]

nums = [1,2,2,2]
print (getsubsetsBFS(nums))

