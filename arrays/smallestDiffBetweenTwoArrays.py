def smallestDifference(a, b):
    # Write your code here.
    # -1, 3, 5, 10, 20, 28
	# 15, 17, 26, 134, 135
	a.sort()
	b.sort()
	minDiff = float("inf")
	i=0
	j=0
	spair = []
	while i<len(a) and j<len(b):
		first = a[i] #needed as i+=1 overflows if we want to use this post
		second = b[j]
		if (first < second):
			i+=1
		elif (first > second):
			j+=1
		else:
			return [first, second]
		
		diff = abs(first-second)
		
		if diff < minDiff:
			minDiff = diff
			spair = [first,second]
	
	return spair