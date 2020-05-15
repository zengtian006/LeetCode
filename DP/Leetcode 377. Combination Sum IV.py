class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]


# Backtracking
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dic = {}
        self.helper(nums,target, dic)
        return self.helper(nums,target, dic)
    
    def helper(self, nums,target, dic):
        if target == 0:
            return 1 
        if target < 0 :
            return 0
        if target in dic:
            return dic[target]
        count = 0
        for i in range(len(nums)):
            count += self.helper(nums, target-nums[i], dic)
        dic[target] = count
        return count


# Follow up
# If negative numbers exist in input array, then the combinations could be infinite length. For example, nums = [-1, 1] and target = 1. There could have infinite (-1, 1) pairs plus a single 1.
# It will be like [-1,-1,1,1,1] [1], [-1, 1, 1]
# So we have to limit the length of the combination sequence, then problem will have a finite solution.


