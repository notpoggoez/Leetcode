class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(x+y))
            elif tokens[i] == "-":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(y-x))
            elif tokens[i] == "*":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(x*y))
            elif tokens[i] == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(int(y/x))
            else:
                stack.append(tokens[i])
        
        return int(stack[-1])
            

            