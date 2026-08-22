class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = str(n)
        digit = 0
        prod = 1

        for char in n:
            digit += int(char)
            prod *= int(char)
    
        n = int(n)
        return n%(digit+prod)==0