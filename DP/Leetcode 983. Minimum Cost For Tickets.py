class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')]*(days[-1]+1)
        for d in days:
            dp[d] = 0
        dp[0] = 0
        for i in range(1,days[-1]+1):
            if dp[i] == float('inf'):
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]+costs[0]
                dp[i] = min(dp[i], dp[max(0,i-7)]+costs[1]) 
                dp[i] = min(dp[i], dp[max(0,i-30)]+costs[2]) 

        return dp[-1]