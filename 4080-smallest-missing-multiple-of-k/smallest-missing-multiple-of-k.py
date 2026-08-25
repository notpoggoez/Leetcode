class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mult = 1
        while True:
            if k*mult in nums:
                mult +=1 
            else:
                break
        
        return mult*k