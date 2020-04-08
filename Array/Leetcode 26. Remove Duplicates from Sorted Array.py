class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for j in range(len(nums)):
            if j<1 or nums[j]!=nums[j-1]:
                nums[idx] = nums[j]
                idx += 1
        return idx

# 双指针适用in-place modification
# 一个指针（快）遍历，另一个指针（慢）指向下一个要交换的位置，快指针遍历到符合要求的就与慢指针的值交换