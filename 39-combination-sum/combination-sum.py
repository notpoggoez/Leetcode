class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, cur = [],[]
        def dfs(i,total):
            if total > target or i == len(candidates):
                return
            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            total += candidates[i]
            dfs(i, total)
            
            cur.pop()
            total -= candidates[i]
            dfs(i+1, total)
        
        dfs(0,0)
        return res