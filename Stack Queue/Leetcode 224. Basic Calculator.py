class Solution:
    def calculate(self, s: str) -> int:
        stack_sign = []
        stack_num = []
        
        sums = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i< len(s) and s[i].isdigit():
                    num = 10*num + int(s[i])
                    i += 1
                sums += sign*num
            else:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    stack_sign.append(sign)
                    stack_num.append(sums)
                    sums = 0
                    sign = 1
                elif s[i] == ')':
                    sums = stack_num.pop() + stack_sign.pop()*sums
                i+=1
        return sums

        # 遇到'(‘ 记录之前的数和sign
        # 遇到')' 将（）内的和 与 '(' 之前的数 做计算