def get_all_subsets(arr):
    n = len(arr)
    res = []
    for i in range(pow(2,n)):
        subset = []
        for j in range(len(arr)):
            if( i & (1 << j)) > 0:  # for every possible binary representation of 0->2^n-1 we add elements with bits set (1s)
                subset.append(arr[j])
        res.append(subset)
    return res

arr = [1,2,3]
print (get_all_subsets(arr))
arr = [1,2,2]
print (get_all_subsets(arr)) #this approach returns duplicates


from collections import deque

#This approach eliminates duplicates
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
            if lst[:] != prev:#append to queue only when previous in queue != newly picked subset
                queue.append(lst[:])
            if prev != lst + [nums[i]]:#append to queue only when previous in queue != newly picked subset
                queue.append(lst + [nums[i]])
        i += 1
    return list(queue)

nums = [2,2,7,7]
print (getsubsetsBFS(nums)) #this result has no duplicate subsets