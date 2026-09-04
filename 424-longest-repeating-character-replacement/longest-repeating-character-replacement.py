from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l=0

        left = right = 0
        while right < len(s):
            freq[s[right]] +=1 

            while right-left+1 - max(freq.values()) > k:
                freq[s[left]] -=1 
                left+=1 
            
            l = max(l,right-left+1)
            right+=1 
        
        return l