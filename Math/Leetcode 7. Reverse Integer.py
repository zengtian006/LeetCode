class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        res = 0
        while x>0:
            n = x%10
            res = res*10 + n
            if res>2**31 -1 or res <-2**31 :
                return 0
            x //= 10
        return res*sign