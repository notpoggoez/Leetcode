class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        if sum > num * 9:
            return ""
        
        for i in range(9, -1, -1):
            if sum == 0:
                res += "0" * (num - len(res))
                return res 

            while sum - i >= 0:
                res += str(i)
                sum -= i

        return res      