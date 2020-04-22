class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        lb = rb = -1

        # left
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1]!=target:
                    lb = mid
                    break
                else:
                    right = mid -1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if lb == -1:return [-1,-1]
        # right
        right = n-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                if mid == n-1 or nums[mid+1]!=target:
                    rb = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if rb == -1:return [-1,-1]
        return [lb,rb]