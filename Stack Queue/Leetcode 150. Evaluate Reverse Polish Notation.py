class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                right = int(stack.pop())
                left = int(stack.pop())
                s = 0
                if token == '+':
                    s = right + left
                if token == '-':
                    s = left - right
                if token == '*':
                    s = right * left
                if token == '/':
                    s = math.trunc(left / right)
                stack.append(str(s))
            else:
                stack.append(token)
        return int(stack[-1])