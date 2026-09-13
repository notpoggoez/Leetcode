from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count =0
        freq = defaultdict(list)
        for i in range(len(nums)):
            freq[nums[i]].append(i)
        
        for value in freq.values():
            valid = True
            if len(value) < 3:
                continue 
            
            d = value[1] - value[0]
            for i in range(len(value)-1):
                if value[i] + d != value[i+1]:
                    valid = False
            if valid:
                count+=1 

        return count