class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if -0<n<=2:
            return True
        s = 1
        while s < n:
            s = s*2
            if s ==n:
                return True
        return False