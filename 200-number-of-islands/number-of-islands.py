class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        seen = set()
        d = [(0,1), (0,-1), (-1,0), (1,0)]

        def dfs(i,j):
            if i < 0 or i >= row or j >= col or j < 0 or (i,j) in seen:
                return 
            if grid[i][j] == "0":
                return
            
            seen.add((i,j))
            for dx, dy in d:
                dfs(i+dx, j+dy)
               
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    count +=1 
        
        return count  