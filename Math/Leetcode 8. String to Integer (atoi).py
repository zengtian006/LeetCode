class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        sign = 1
        if str[0] in '+-':
            sign = 1 if str[0] =='+' else -1
            str = str[1:]
        res = 0
        for s in str:
            if not s.isdigit():
                break
            res = res * 10 + int(s)

        res = sign * res
        if res > 2**31 -1:
            return 2**31-1
        if res < -2**31:
            return -2**31
        return res