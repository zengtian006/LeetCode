# Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            idx = self.findFisrtLarge(num, stack)
            if idx == -1:
                stack.append(num)
            else:
                stack[idx] = num
        return len(stack)
    
    def findFisrtLarge(self, target, nums):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                if mid == 0 or nums[mid-1]<target:
                    return mid
                else:
                    right = mid -1
            else:
                left = mid +1
        return -1
        
        
# DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        for j in range(1, n):
            for i in range(j):
                if nums[j]> nums[i]:
                    dp[j] = max(dp[j],dp[i]+1)
        return max(dp)