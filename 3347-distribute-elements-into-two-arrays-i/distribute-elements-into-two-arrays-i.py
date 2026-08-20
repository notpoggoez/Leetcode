class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        stack1 = [nums[0]]
        stack2 = [nums[1]]
        res = []
        for i in range(2, len(nums)):
            x = stack1[-1]
            y = stack2[-1]

            if x > y:
                stack1.append(nums[i])
            else:
                stack2.append(nums[i])
        
        for i in range(len(stack1)):
            res.append(stack1[i])
        for i in range(len(stack2)):
            res.append(stack2[i])

        return res


        