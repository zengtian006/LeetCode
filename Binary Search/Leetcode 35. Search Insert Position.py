class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid]>=target:
                if mid == 0 or nums[mid-1]<target:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return right + 1