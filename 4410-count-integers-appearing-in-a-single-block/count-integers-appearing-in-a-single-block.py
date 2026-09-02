class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = 0
        seen = set()
        subtract = set()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue            
            if nums[i] in seen:
                subtract.add(nums[i])
            else:
                count+=1 
                seen.add(nums[i])

        if nums[-1] in seen:
            subtract.add(nums[-1])
        else:
            count+=1 
        
        count -= len(subtract)
        return count     