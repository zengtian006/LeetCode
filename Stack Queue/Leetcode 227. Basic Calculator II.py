class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        i,sign,num = 0, '+', 0
        while i < len(s):
            if s[i].isdigit():
                while s[i].isdigit() and i<len(s):
                    num = num*10 + int(s[i])
                    i += 1
            else:
                if s[i] in '+-*/':
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        temp = stack.pop()*num
                        stack.append(temp)
                    elif sign == '/':
                        temp = math.trunc(stack.pop()/num)
                        stack.append(temp)
                    num = 0
                    sign = s[i]
                i += 1
        return sum(stack)