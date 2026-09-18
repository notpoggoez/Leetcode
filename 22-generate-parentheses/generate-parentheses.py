class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dfs(x):
            if x.count("(") > n:
                return
            if x.count(")") > x.count("("):
                return 
            if len(x) == 2*n:
                res.append(x)
                return
            
            x+= "("
            dfs(x)
            x = x[:-1]
            x += ")"
            dfs(x)
        
        dfs("")
        return res