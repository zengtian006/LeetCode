class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s and n > 1:
            s.add(n)
            k = n
            res = 0
            while k > 0:
                res += (k%10)**2
                k //=10
            n = res
        return n == 1