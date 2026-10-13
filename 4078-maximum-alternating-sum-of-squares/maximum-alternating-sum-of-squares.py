class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1 
        res = count = 0
        even = False 
        
        if len(nums)%2 == 0:
            even = True
        

        while left <= right:
            while left <= right and even and count >= len(nums)/2:
                res -= nums[left]**2 
                left+=1 
            
            while left <= right and not even and count > len(nums)//2:
                res -= nums[left]**2 
                left+=1 
            
            if left <= right and abs(nums[left]) > abs(nums[right]):
                res += nums[left]**2 
                left+=1 
            elif left <= right and abs(nums[right]) >= abs(nums[left]):
                res += nums[right]**2 
                right -=1
        
            count +=1 
        
        return res