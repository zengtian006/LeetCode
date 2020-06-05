class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i>=2 else 0) - prices[i])
        return dp[-1][0]

# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) 第i天手上沒有股票， 有兩種可能，1，前一天就没股票，2， 第i天把股票卖了
# dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i>=2 else 0) - prices[i])， 第i天手上有股票，有3种可能，1，前一天就有股票，2，前两天没有股票，第i天买了第一支股票 3，前一天什么也没做，第i天买了第一支股票