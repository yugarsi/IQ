#calculate number of islands
#O(R*C) R= number of rows and C=number of columns, both
#Space also O(R*C)
class Solution:
    self.numvisited = 0
    def dfs(self, grid, i, j): #counting no of connected components
        nr = len(grid)
        nc = len(grid[0])
        if (i < 0 or j < 0 or i >=nr or j >=nc or grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'
        self.dfs(grid, i-1, j)
        self.dfs(grid,i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid,i, j+1)
        
            
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,i,j)
        
        return count