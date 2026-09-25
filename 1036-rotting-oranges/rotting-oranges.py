from collections import deque 
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        total = time = 0
        seen = set()
        q = deque()
        row, col = len(grid), len(grid[0])
        d = [(1,0), (0,1), (-1,0), (0, -1)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    total +=1 
        if total == 0:
            return 0
         
        while q:
            for i in range(len(q)):
                y,x = q.popleft()
                for dy, dx in d:
                    if 0 <= y +dy < row and 0<= x+dx < col and (y+dy, x+dx) not in seen and grid[y+dy][x+dx] != 0:
                        q.append([y+dy, x+dx])
                        seen.add((y+dy,x+dx))
                        total -=1 
              
            time +=1 
            if total <= 0:
                return time 
        
        return -1