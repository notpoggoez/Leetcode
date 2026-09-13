from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count =0
        freq = defaultdict(list)
        for i in range(len(nums)):
            freq[nums[i]].append(i)
        
        for value in freq.values():
            if len(value)!= 3:
                continue
            
            if value[2] - value[1] == value[1] - value[0]:
                count +=1 
        
        return count    