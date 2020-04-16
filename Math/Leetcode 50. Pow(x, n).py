class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = abs(n)
        res = 1
        while n >0:
            if n%2 == 1:
                res *= x
            x *=x
            n //= 2
        return res
    
    
   # 2^8 = 4^4
   # 2^9 = 2*4^4 