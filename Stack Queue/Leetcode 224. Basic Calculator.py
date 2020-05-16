class Solution:
    def calculate(self, s: str) -> int:
        sums_stack = []
        sign_stack = []
        sums = 0
        sign = 1
        num = 0
        s+='+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 +int(s[i])
            elif s[i] == '+':
                sums += sign*num
                sign = 1
                num = 0
            elif s[i] == '-':
                sums += sign*num
                sign = -1
                num = 0
            elif s[i] == '(':
                sums_stack.append(sums)
                sign_stack.append(sign)
                sums = 0
                sign = 1
            elif s[i] == ')':
                sums += sign*num
                num = 0
                sums = sums_stack.pop() + sign_stack.pop()*sums
        return sums

        # 遇到'(‘ 记录之前的数和sign
        # 遇到')' 将（）内的和 与 '(' 之前的数 做计算