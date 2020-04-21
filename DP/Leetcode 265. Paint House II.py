class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        m, k = len(costs), len(costs[0])
        dp = [[0]*k for _ in range(m)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for i in range(1,m):
            for j in range(k):
                min_pre = float('inf')
                for h in range(k):
                    if h != j:
                        min_pre = min(min_pre, dp[i-1][h])
                dp[i][j] = min_pre+costs[i][j]
        return min(dp[-1])