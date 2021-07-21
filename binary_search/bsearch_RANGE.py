def bsearchRange (arr, start, end, target, frange, goleft):
	while start <= end:
		mid = (start + end)//2
		if arr[mid] < target:
			start = mid+1
		elif arr[mid] > target:
			end = mid - 1
		else:
			if goleft:
				if mid==0 or arr[mid-1]!= target:
					frange[0] = mid
					return
				else:
					end = mid-1 #go left
			else: #going right
				if mid == len(arr)-1 or arr[mid+1] != target:
					frange[1]=mid
					return
				else:
					start = mid +1 #go right
def searchForRange(arr, target):
    finalRange = [-1, -1]
	bsearchRange(arr, 0, len(arr)-1, target, finalRange, True)
	bsearchRange(arr, 0, len(arr)-1, target, finalRange, False)
	return finalRange
	
