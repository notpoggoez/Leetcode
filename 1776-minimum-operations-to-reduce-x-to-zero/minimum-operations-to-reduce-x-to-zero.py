class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        longest = -1 
        cur = 0

        total = sum(nums)
        target = total -x 

        if target < 0:
            return -1 
        left = right = 0

        while right < len(nums):
            cur += nums[right]
            while cur > target: 
                cur -= nums[left] 
                left +=1 
            
            if cur == target:
                longest = max(longest, right-left+1)

            
            right +=1 
        
        return -1 if longest == -1 else len(nums) - longest    