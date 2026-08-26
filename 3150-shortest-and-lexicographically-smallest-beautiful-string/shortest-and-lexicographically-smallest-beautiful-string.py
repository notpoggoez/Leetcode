class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 100
        res = ""
        index = []
        total  = 0
        for i in range(len(s)):
            if s[i] == "1":
                index.append(i)
                total+=1
        if total < k:
            return  ""
        
        for i in range(len(index)-k+1):
            start = index[i]
            end = index[i+k-1]
            cur = s[start:end+1]

            if end - start +1 < l:
                l = index[i+k-1] - index[i] +1
                res = cur 
            elif index[i+k-1] - index[i] +1 == l:
                if cur < res or res == "":
                    res = cur
        
        return res
        
                
        

        