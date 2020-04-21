class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]


# Backtracking (TLE)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = []
        self.bt(nums, [], target, res)
        return len(res)
        
    def bt(self, nums, tempList, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(tempList)
            return
        for i in range(len(nums)):
            self.bt(nums, tempList+[nums[i]], target - nums[i], res)