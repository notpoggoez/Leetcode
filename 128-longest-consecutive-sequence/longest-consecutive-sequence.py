class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        present = set(nums)
        l=0
        for num in present:
            if num-1 in present:
                continue
            cur = 1
            while num +1 in present:
                cur +=1 
                num +=1 

            l = max(l,cur)
        
        return l