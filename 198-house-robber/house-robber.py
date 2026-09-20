class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        nums[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i]+ nums[i-2], nums[i]+nums[i-3])
        
        return max(nums[n], nums[n-1])