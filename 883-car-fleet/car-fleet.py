class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort()
        for i in range(len(arr)):
            while stack:
                if (target - stack[-1][0])/stack [-1][1] <= (target-arr[i][0])/arr[i][1]:
                    stack.pop()
                else:
                    break
            stack.append((arr[i][0], arr[i][1]))

        return len(stack)