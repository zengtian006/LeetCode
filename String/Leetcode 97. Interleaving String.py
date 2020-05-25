class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1),len(s2)
        if l1+l2!= len(s3):
            return False
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        dp[0][0] = 1
        
        for i in range(l1+1):
            for j in range(l2+1):
                k = i+j-1
                if i>0 and dp[i-1][j] and s3[k] == s1[i-1]:
                    dp[i][j] = 1
                elif j>0 and dp[i][j-1] and s3[k] == s2[j-1]:
                    dp[i][j] = 1
        return dp[-1][-1]