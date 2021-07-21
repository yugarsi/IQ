class Solution:
    #treat the 2D matrix like a graph and DFS/BFS from the start points
    #using DFS
    def floodFill(self, image, startRow, startCol, newColor):
        R = len(image)
        C = len(image[0])
        color = image[startRow][startCol]
        if color == newColor: #base case , color to fill same as what you clicked then nothing to do
            return image

        #this is the DFS function which will call later
        #you don't need a set to mark visited as
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(startRow, startCol)
        return image
##################################################################################
#https://codeinterview.io/YYZNEFEHOX
#Using BFS
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        if color == newColor:
            return image

        R = len(image)
        C = len(image[0])
        queue = [(sr, sc)]

        while queue:
            r, c = queue.pop()
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    queue.append((r - 1, c))
                if r + 1 < R:
                    queue.append((r + 1, c))
                if c >= 1:
                    queue.append((r, c - 1))
                if c + 1 < C:
                    queue.append((r, c + 1))

        return image

