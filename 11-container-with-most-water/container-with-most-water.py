class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        h = 0

        while l < r:
            h = max((r-l)*min(height[l],height[r]), h)
            if height[l] == min(height[l], height[r]):
                l+=1 
            else:
                r-=1 
        
        return h    