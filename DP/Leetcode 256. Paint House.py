class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: 
            return 0
        m = len(costs)
        dp = [[0]*3 for _ in range(m)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, m):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + costs[i][2]
        return min(dp[-1])