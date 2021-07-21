      
#easy algo to find one (1) closest item to a target
# not just exact match
def findClosest(arr, target):
    n = len(arr)
    if n < 1:
        return - 1
    if target < arr[0]:  #edge cases
        return arr[0]
    if target > arr[n-1]:
        return arr[n-1]

    start = 0
    end = n-1
    mindiff = float("inf")
    minval = arr[0]

    while (start <= end):
        mid = (start+end)//2
        if arr[mid] == target:
            return arr[mid]
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid + 1
        diff = abs(arr[mid]-target)
        if diff < mindiff:
            mindiff = diff
            minval = arr[mid]

    return minval
