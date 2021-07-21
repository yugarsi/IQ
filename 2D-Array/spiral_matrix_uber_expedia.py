'''
1 1 1 1 1   each for loop limits until unique numbers
0       3
0       3
0 2 2 2 3
'''

class Solution:
    def spiralOrder(self, matrix):
        output = []
        if len(matrix) == 0:
            return output
        r1, r2 = 0, len(matrix) - 1 #max row limits of indices upto which to traverse
        c1, c2 = 0, len(matrix[0]) - 1 #max column index to traverse

        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                output.append(matrix[r1][c])
            for r in range(r1 + 1, r2 + 1):
                output.append(matrix[r][c2])

            if (r1 < r2 and c1 < c2):
                for c in range(c2 - 1, c1, -1):
                    output.append(matrix[r2][c])
                for r in range(r2, r1, -1):
                    output.append(matrix[r][c1])

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return output
