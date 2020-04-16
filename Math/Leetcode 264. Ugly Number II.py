class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2 = i3 = i5 =0
        while n > 1:
            mn = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            if mn == dp[i2]*2:
                i2 += 1
            if mn == dp[i3]*3:
                i3 += 1
            if mn == dp[i5]*5:
                i5 += 1
            dp.append(mn)
            n -= 1
        return dp[-1]