class Solution:
    
    # down-top
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
            
        for left in range(n-1,-1,-1):
            for right in range(left+1,n):
                if s[left]==s[right]:
                    dp[left][right] = 2+dp[left+1][right-1]
                else:
                    dp[left][right] = max(dp[left+1][right],dp[left][right-1])
        return dp[0][-1]