class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if 1<=int(s[0])<=9 else 0
        for i in range(2,len(s)+1):
            if 10<=int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
            if 0<int(s[i-1:i])<10:
                dp[i] += dp[i-1] 
        return dp[-1]