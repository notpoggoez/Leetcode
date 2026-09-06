from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        res = []
        
        for i in range(len(strs)):
            mapping = [0]*26
            for c in strs[i]:
                mapping[ord(c) - ord('a')] +=1 
            
            mapping = tuple(mapping)
            freq[mapping].append(strs[i])
        
        for value in freq.values():
            res.append(value)
        
        return res