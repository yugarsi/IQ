'''
Maximum Sum Submatrix
You're given a two-dimensional array (a matrix) of potentially unequal height and
 width that's filled with integers. You're also given a positive integer size. 
 Write a function that returns the maximum sum that can be generated from a submatrix with
  dimensions size * size.
For example, consider the following matrix:
[
  [2, 4],
  [5, 6],
  [-3, 2],
]
If size= 2, then the 2x2 submatrices to consider are:
[2, 4]
[5, 6]
------
[5, 6]
[-3, 2]
The sum of the elements in the first submatrix is 17, and the sum of the elements in the second submatrix is 10. 
In this example, your function should return 17.

Note: size will always be at least 1, and the dimensions of the input matrix will always be at least size * size.

'''
def maximumSumSubmatrix(matrix, size):
	#modify the given matrix with sum upto that point
	#which is left + top - diag (diag is added twice so needs to be subtracted once
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			left = matrix[r-1][c] if r > 0 else 0
			top = matrix[r][c-1] if c > 0 else 0
			diag = matrix[r-1][c-1] if r > 0 and c > 0 else 0
			matrix[r][c] += left + top - diag
	
	maxsum = -float("inf")
	for r in range(size-1, len(matrix)): #because size-1
		for c in range(size-1, len(matrix[0])):
			left = matrix[r-size][c] if r-size >= 0 else 0 #
			top = matrix[r][c-size]  if c-size >=0 else 0
			diag = matrix[r-size][c-size] if r-size>=0 and c-size>=0 else 0
			cursum = matrix[r][c] - top - left + diag
			maxsum = max(maxsum,cursum)
	
	return maxsum