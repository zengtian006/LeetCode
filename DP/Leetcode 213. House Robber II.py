class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        wo_first = nums[1:]
        wo_last = nums[:-1]
        n = len(nums)-1
        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0] = wo_first[0]
        dp2[0] = wo_last[0]
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], wo_first[i] + (dp1[i-2] if i>1 else 0) )
            dp2[i] = max(dp2[i-1], wo_last[i] + (dp2[i-2] if i>1 else 0) )
        return max(dp1[-1], dp2[-1])