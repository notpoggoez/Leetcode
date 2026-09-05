class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        
        largest = 0
        for i in range(len(nums)):
            largest = max(largest, nums[i])
            if largest - suffix[i] <= k:
                return i
        
        return -1