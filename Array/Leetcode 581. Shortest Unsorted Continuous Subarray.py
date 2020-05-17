class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left = len(nums)
        right = 0
        for i in range(len(nums)):
            while stack and nums[i]<nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)
        return right-left+1 if right>left else 0
        