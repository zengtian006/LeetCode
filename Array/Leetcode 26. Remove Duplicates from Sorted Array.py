class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1

# 双指针适用in-place modification
# 一个指针（快）遍历，另一个指针（慢）指向下一个要交换的位置，快指针遍历到符合要求的就与慢指针的值交换