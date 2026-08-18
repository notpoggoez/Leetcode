from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k != len(nums):
            freq = defaultdict(int)
            for num in nums:
                freq[num] +=1 
            
            if k == 1:
                res = -1 
                for key,value in freq.items():
                    if value == 1 and key > res:
                        res = key 
                
                return res 

            x = nums[0]
            y = nums[-1]
            if freq[x] == 1 and freq[y] == 1:
                return max(x,y)
            elif freq[x] > 1 and freq[y] == 1:
                return y
            elif freq[x] == 1 and freq[y] > 1:
                return x
            else:
                return -1
        else:
            return max(nums)     