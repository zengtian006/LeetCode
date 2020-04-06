class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx,count = 0, 0
        for j in range(len(nums)):
            if count<2:
                nums[idx] = nums[j]
                idx += 1
            if j == len(nums)-1 or nums[j] == nums[j+1]:
                count += 1
            elif nums[j] != nums[j+1]:
                count = 0
        return idx