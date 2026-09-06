class Solution:
    def countRotations(self, s: str, k: int) -> int:
        score = 0
        n = len(s)

        for i in range(n-1):
            if s[i] == s[i+1]:
                score += 1
                
        if s[0] == s[-1]:
            score +=1

        if (score - 1) == k:
            return score
        elif (score == k):
            return n - score
        else:
            return 0