class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        left = 0
        right = len(height)-1 
        lmax = height[left]
        rmax = height[right]

        while left < right:
            curr = min(lmax, rmax)
            if height[left] < height[right]:
                left +=1 
                lmax = max(lmax, height[left])
                if height[left] < curr:
                    count += curr - height[left]
            else:
                right -=1 
                rmax = max(rmax, height[right])
                if height[right] < curr:
                    count += curr - height[right]
        return count    