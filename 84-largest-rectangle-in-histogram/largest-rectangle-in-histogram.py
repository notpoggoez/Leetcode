class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0 
        smallestr = [-1]*len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < stack[-1][0]:
                stack.pop()
            
            if not stack:
                smallestr[i] = -1
            else:
                smallestr[i] = stack[-1][1] - i
            
            stack.append((heights[i], i))
        
        smallestl = [-1] *len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            
            if not stack:
                smallestl[i] = -1
            else:
                smallestl[i] = i - stack[-1][1] -1
            
            stack.append((heights[i], i))

            if smallestl[i] == -1:
                l = i
            else:
                l = smallestl[i]
            
            if smallestr[i] == -1:
                r = len(heights) - i 
            else:
                r = smallestr[i]
                
            area = max(area, heights[i] * (r+l))
        
        return area