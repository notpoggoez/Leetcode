import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        
        while count < k:
            res = heapq.heappop(nums)
            count+=1 
        
        return -res