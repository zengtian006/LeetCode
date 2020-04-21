class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dic = set(wordDict)
        for j in range(1,len(s)+1):
            for i in range(j):
                if dp[i] == 1 and s[i:j] in dic:
                    dp[j] = 1
        return dp[-1]