class Solution:
    def minimumMoves(self, A):
        dp = [[len(A) for i in A] for j in A]
        for i in range(len(A)):
            dp[i][i] = 1
        for i in range(len(A)-1):
            dp[i][i+1] = 1 if A[i] == A[i+1] else 2
        
        for size in range(3,len(A)+1):
            for l in range(len(A)-size+1):
                r = l+size-1
                if A[l] == A[r]:
                    dp[l][r] = dp[l+1][r-1]
                for mid in range(l, r):
                    dp[l][r] = min( dp[l][r], dp[l][mid]+dp[mid+1][r])
        return dp[0][len(A)-1]