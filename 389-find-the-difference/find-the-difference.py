from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqs = defaultdict(int)
        freqt = defaultdict(int)
        
        for char in s:
            freqs[char] +=1 
        for char in t:
            freqt[char] +=1 
        
        for key, value in freqt.items():
            if key not in s or freqs[key]!= value:
                return key 