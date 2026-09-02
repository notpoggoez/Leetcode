class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        count = 0

        for i in range(len(nums)):
            width = nums[i]%10
            d = str(nums[i]//10)
            
            x = int(d[:width])
            y = int(d[width:])
            count = (count + pow(x,y,mod))%mod
        
        return count%mod