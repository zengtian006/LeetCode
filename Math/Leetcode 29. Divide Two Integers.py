class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31:
            if divisor == -1:
                return 2**31-1
            if divisor == 1:
                return dividend
        if dividend == 2**31-1 and divisor == 1:
            return dividend
        
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        res = 0
        while dividend - divisor>=0:
            shift = 0
            while dividend>=(divisor<<shift):
                shift+=1
            res+=1<<(shift-1)
            dividend -= divisor<<(shift-1)
        return res*sign