res = []

#In subarray problem  appending to global list in recursion is problematic
def getSubArrays(arr, curindex):
    if curindex == len(arr):
        return

    subarr = []
    for i in range(curindex, len(arr)):
        subarr.append(arr[i])
        print (subarr) #print is possible but appending to res will create problems
    getSubArrays(arr, curindex+1)


# n * (n+1)/2 subarrays
#getSubArrays([1,2,3], 0)

#iterative approach
def getsubArraysIter(arr):
    n = len(arr)
    res = []
    for i in range(n):
        j = i+1
        while j <= n:
            sub = arr[i:j]  #subarray everytime i -> n and move j from i+1 -> n
            res.append(sub)
            j+=1

    return res

print(getsubArraysIter([1,2,3]))
