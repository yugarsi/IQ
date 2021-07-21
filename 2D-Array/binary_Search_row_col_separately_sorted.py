# worse case when n==m and large where in m is row num and n is column number
# Search both row and column wise  O(log(n!)) = O(nlogn)
# space complexity = O(1) i.e. no extra additional space needed except few constants
class Solution:
    # Algorithm

    # searching both vertically and row wise
    # if is vertical is true do binary binary_search on the column
    def binarysearch(self, matrix, start, target, rowsearch):
        left = start

        right = len(matrix) - 1
        if rowsearch:  # searching within a row then
            right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            # if row binary_search is true binary_search column wise within a "single" row i.e. row=constant
            if rowsearch:
                if matrix[start][mid] == target:  # note start stays const diff from left and right
                    return True
                elif matrix[start][mid] > target:  # target is smaller move right to left of mid
                    right = mid - 1
                else:
                    left = mid + 1

            # if rowsearch is false binary_search within a single column, with columnno=start
            else:

                if matrix[mid][start] == target:
                    return True

                elif matrix[mid][start] > target:

                    right = mid - 1
                else:
                    left = mid + 1

        return False

    def searchMatrix(self, matrix, target: int) -> bool:

        R = len(matrix)  # no of rows
        C = len(matrix[0])  # no of cols

        # iterate to minimum of row or column
        for i in range(min(R, C)):  # run start index to
            rowfound = self.binarysearch(matrix, i, target, True)  # binary_search row
            colfound = self.binarysearch(matrix, i, target, False)  # binary_search column
            if rowfound or colfound:
                return True

        return False

#above one isn't most optimal
# O (M + N) solution called (binary_search space reduction)
'''
1 4 7 9 15
2 14 21 32
6 8  12  34

Algo = 
start searching from bottom left
1. if target > current_index go right
2. elif target < current_index go top
3. else its found
  
'''
######################
class Solution(object):
    def searchMatrix(self, matrix, target):
        R = len(matrix)
        if R == 0:
            return False

        C = len(matrix[0])
        if C == 0:
            return False

        r = R - 1  # bottom left row index #Remember the R-1!!
        c = 0  # bottom left col index

        while c < C and r >= 0:  # col goes left to right and row from bottom to top
            if matrix[r][c] > target:  # go top if target is smaller
                r -= 1
            elif matrix[r][c] < target:  # go right if target is greater
                c += 1
            else:
                return True

        return False

