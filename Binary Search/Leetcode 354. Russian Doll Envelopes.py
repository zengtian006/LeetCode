# Binary Search
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for envelope in envelopes:
            idx = self.findFisrtLarge(envelope, stack)
            if idx == -1:
                stack.append(envelope[1])
            else:
                stack[idx] = envelope[1]
        return len(stack)
        
    def findFisrtLarge(self, target, stack):
        left, right = 0, len(stack)-1
        while left <= right:
            mid = left + (right-left)//2
            if stack[mid]>=target[1]:
                if mid == 0 or stack[mid-1]<target[1]:
                    return mid
                else:
                    right = mid -1
            else:
                left = mid + 1
        return -1
            
            
            
# DP (TLE)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: x[0])
        n = len(envelopes)
        dp = [1]*n
        for j in range(1, n):
            for i in range(j):
                if envelopes[j][1]>envelopes[i][1] and envelopes[j][0]>envelopes[i][0]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)