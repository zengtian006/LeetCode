class Solution:
    def decodeString(self, s: str) -> str:
        stack_mul = []
        stack_char = []
        mul = 0
        strr = ''
        for char in s:
            if char.isdigit():
                mul = 10*mul + int(char)
            elif char.isalpha():
                strr += char
            elif char == '[':
                stack_mul.append(mul)
                stack_char.append(strr)
                mul = 0
                strr = ''
            elif char == ']':
                m = stack_mul.pop()
                strr = stack_char.pop() + strr * m
        return strr

        # 遇到'[' 记录之前的strr 和 muli_num
        # 遇到']' 将目前的strr 与 之前的mul_num相乘 在加上之前的strr