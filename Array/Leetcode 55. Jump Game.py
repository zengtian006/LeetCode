class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range(1,len(nums)):
            if farthest>=i:
                farthest = max(farthest, nums[i]+i)
        return farthest>=len(nums)-1


# 从第一个数开始，计算farthest范围内的farthest。最后如果farthest超过数组，则return True