class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n
        while left<=right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                if mid == 0 or not isBadVersion(mid-1):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1