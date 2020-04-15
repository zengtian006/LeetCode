class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]  #dp[m+1][n+1] means s[:m+2] t[:n+2]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]  #drop s[i]
        return dp[-1][-1]
    
    
    #    0 r a b b i t
    # 0  1 0 0 0 0 0 0
    # r  1 1 0 0 0 0 0
    # a  1 1 1 0 0 0 0
    # b  1 1 1 1 0 0 0
    # b  1 1 1 2 1 0 0
    # b  1 1 1 3 3 0 0
    # i  1 1 1 3 3 3 0
    # t  1 1 1 3 3 3 3