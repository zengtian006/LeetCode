class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')':
                if i>0 and s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                if i>0 and s[i-1] == ')':   #(())
                    if i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 
        return max(dp)

# 求极值 考虑DP