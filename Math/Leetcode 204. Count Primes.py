class Solution:
    def countPrimes(self, n: int) -> int:
        p = [1]*n
        res = 0
        for i in range(2,n):
            if p[i] == 1:
                res +=1
            j = 2
            while i*j<n:
                p[i*j] =0
                j += 1
        return res