class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = min(nums[0], nums[-1])
        left = 0
        right = len(nums)-1 

        if nums[left] < nums[right]:
            return nums[0]
        
        while left <= right:
            mid = (left+right)//2 

            if nums[mid] > nums[left]:
                left = mid + 1 
                smallest = min(smallest, nums[left])
            else:
                smallest = min(smallest, nums[mid])
                right = mid - 1
                smallest = min(smallest, nums[right])
        
        return smallest    