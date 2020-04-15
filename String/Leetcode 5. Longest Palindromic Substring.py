class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        max_len = 0
        res = ''
        for i in range(len(s)):
            dp[i][i] = 1
            max_len = 1
            res = s[i]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                res = s[i:i+2]
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        res = s[i:j+1]
        return res