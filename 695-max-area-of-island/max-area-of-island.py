class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        largest = 0
        row = len(grid)
        col = len(grid[0])
        
        seen = set()
        d = [(1,0), (-1,0), (0,-1), (0,1)]

        def dfs(i,j):
            if i >= row or i < 0 or j >= col or j < 0 or (i,j) in seen or grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            area = 1
            for dx, dy in d:
                area += dfs(i+dx, j+dy)
            
            return area 
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in seen:
                    val = dfs(i,j)
                    largest = max(largest,val)
        
        return largest