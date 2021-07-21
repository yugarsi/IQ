'''
binary binary_search in 2D-array
Write an efficient algorithm that searches for a value in an m x n matrix.

Here every thing is in order so you can treat as one array using a math trick

'''

# In this case the array is fully sorted so treat 2d array as flat one-D array and use the trick below
class Solution:
    # Here both row and column
    def searchMatrix(self, matrix, target: int) -> bool:

        R = len(matrix)
        if R == 0:
            return False  # base case

        C = len(matrix[0])  # total no of columns

        start = 0
        end = R * C - 1  # last index assuming it were a straight array

        #regular binary binary_search with a trick
        # note matrix[index // C][index % C] gives element in 2d array
        # when flattened from 0 --> R*C - 1 indices
        while start <= end:
            mid = (start + end) // 2
            midelement = matrix[mid // C][mid % C]  # this formula is the trick
            if target == midelement:
                return True
            elif target > midelement:
                start = mid + 1
            else:
                end = mid - 1

        return False
