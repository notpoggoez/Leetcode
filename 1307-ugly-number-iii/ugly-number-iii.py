import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2*10**9
        
        while left <= right:
            mid = (left+right)//2 
            if mid//a + mid//b + mid//c - mid//(math.lcm(a,b)) - mid//(math.lcm(a,c)) - mid//(math.lcm(b,c)) + mid//(math.lcm(a,b,c)) < n: 
                left = mid+1
            elif mid//a + mid//b + mid//c - mid//(math.lcm(a,b)) - mid//(math.lcm(a,c)) - mid//(math.lcm(b,c)) + mid//(math.lcm(a,b,c)) > n:
                right = mid-1
            else:
                right = mid -1
            
        return left