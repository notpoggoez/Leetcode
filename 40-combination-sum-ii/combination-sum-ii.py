class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res, cur = [],[]
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            total += candidates[i]
            dfs(i+1, total)

            cur.pop()
            total -= candidates[i]
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1 

            dfs(i+1, total)
        
        dfs(0,0)
        return res