class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right-left)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid - 1