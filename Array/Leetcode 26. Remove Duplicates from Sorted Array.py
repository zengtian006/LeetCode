class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for j in range(len(nums)):
            if j<1 or nums[j]!=nums[j-1]:
                nums[idx] = nums[j]
                idx += 1
        return idx