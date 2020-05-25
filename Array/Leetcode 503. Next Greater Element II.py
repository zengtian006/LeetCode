class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        res = [-1]*len(nums)
        for i in range(1,len(nums)*2):
            i %= len(nums)
            while stack and nums[i]>nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        return res
                
                