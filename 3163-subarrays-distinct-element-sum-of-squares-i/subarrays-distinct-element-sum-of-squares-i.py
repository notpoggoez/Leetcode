class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            freq = {}
            length = 0
            for j in range(i, len(nums)):
                if nums[j] not in freq:
                    length+=1 
                    freq[nums[j]] = 1
                else:
                    freq[nums[j]] +=1 

                res += length**2 
                 
        return res