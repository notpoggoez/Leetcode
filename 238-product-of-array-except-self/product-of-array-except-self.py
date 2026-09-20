class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        prefix = [1]*len(nums)
        suffix = [1] * len(nums)
        prefix[0], suffix[-1] = nums[0], nums[-1]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        
        res.append(suffix[1])
        for i in range(1, len(nums)-1):
            res.append(prefix[i-1]*suffix[i+1])
        
        res.append(prefix[len(prefix)-2])
        
        return res