class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0
        seen = set()
        row = len(board)
        col = len(board[0])
        d = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col or (i,j) in seen or board[i][j] == ".":
                return
            seen.add((i,j))

            for dx, dy in d:
                dfs(i+dx, j+dy)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "X" and (i,j) not in seen:
                    dfs(i,j)
                    count +=1 
        
        return count