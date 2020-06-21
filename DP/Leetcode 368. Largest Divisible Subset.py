class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dic = collections.defaultdict(list)
        dp = [[num] for num in nums]
        maxLen = 1
        idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j]+[nums[i]]
                    if len(dp[i])>maxLen:
                        maxLen = len(dp[i])
                        idx = i
        return dp[idx]



# https://www.youtube.com/watch?v=6WRuJzsw1TE