class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(":")", "[":"]", "{":"}"}
        stack = []

        for val in s:
            if val in mapping:
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                if mapping[stack[-1]] == val:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0