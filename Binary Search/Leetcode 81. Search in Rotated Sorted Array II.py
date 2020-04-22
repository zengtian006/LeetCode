class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[right]:
                if nums[left]<=target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[right]:  #2,2,2,5,2,2
                right -= 1
        return False