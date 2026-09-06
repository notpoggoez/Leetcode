class Solution:
    def countRotations(self, s: str, k: int) -> int:
        count = 0
        possible = []

        for i in range(len(s)):
            new = s[0]
            shifted = s[1:] + new
            possible.append(shifted)
            s = shifted
        
        for i in range(len(possible)):
            curr = 0
            for j in range(len(possible[i])-1):
                if possible[i][j] == possible[i][j+1]:
                    curr +=1 
            
            if curr == k:
                count+=1 
        
        return count       