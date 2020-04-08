class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0
        if k>n/2:
            res=0
            for i in range(1,n):
                res+=max(0,prices[i]-prices[i-1])
            return res
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]

        for i in range(n):
            for j in range(1,k+1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][1] + prices[i], dp[i-1][j][0])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]



# DP[n][k][0]  在第n天 最多進行k次交易 手上沒有股票， DP[n][k][1] 在第n天 最多進行k次交易 手上沒有股票
# Base case是：第dp[0][j][0]和dp[0][j][1]  第一天 沒股票肯定是0，第一天有股票肯定是買入了第一天的股票
# 所以dp的转化公式是 
# dp[i][j][0] = max(dp[i-1][j][1] + prices[i], dp[i-1][j][0]) 第i天进行j次交易后手上没有股票，有两种可能，一是前一天手上有股票，第i天卖掉了，另外一种可能是前一天也没股票，第i天什么也没做
# dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) 第i天进行j次交易后手上有股票，有两种可能，一是前一天手上有股票，第i天什么也没做，另外一种可能是前一天没股票，第i天买入了
