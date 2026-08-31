import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = max(piles)
        while left <= right:
            count = 0
            mid = (left+right)//2 

            for i in range(len(piles)):
                count += math.ceil(piles[i]/mid)
            
            if count > h:
                left = mid +1
            elif count <= h:
                k = min(k,mid)
                right = mid - 1
        
        return k