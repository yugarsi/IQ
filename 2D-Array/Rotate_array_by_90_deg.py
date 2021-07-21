class Solution:
    def rotate(self, matrix) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    #transposing [a[i][j] = a[j][i] along diagonal  +  relect rotates matrix by 90 degrees
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
