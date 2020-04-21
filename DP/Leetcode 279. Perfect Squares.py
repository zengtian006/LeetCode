class Solution:
    def numSquares(self, n: int) -> int:
        ps_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            for num in ps_nums:
                if i>=num:
                    dp[i] = min(dp[i], dp[i-num]+1)
        return dp[n]