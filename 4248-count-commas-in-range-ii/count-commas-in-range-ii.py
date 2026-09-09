class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if n < 1000:
            return 0
        
        index = 0
        for i in range(1,10):
            if 1000**i > n:
                index = i-1
                break
        
        for i in range(1,index):
            count += (1000**(i+1) - 1000**i)*i  
        count +=  (n - 1000**index +1)*index
        return count