class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            #this is conditionn when to return 0.. all true then a not
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        
        maxA = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ar = area(r, c)
                if ar > maxA:
                    maxA = ar
        
        return maxA
                    