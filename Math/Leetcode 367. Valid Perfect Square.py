class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 1, num//2
        while left <= right:
            mid = left + (right-left)//2
            if mid*mid == num:
                return mid
            if mid*mid > num:
                right = mid-1
            if mid*mid < num:
                left = mid +1
        return False