class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        left = 0 
        right = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                l = max(l, right-left+1)
                right+=1 
            else:
                seen.discard(s[left])
                left+=1 
        return l