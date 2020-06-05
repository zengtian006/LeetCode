class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [0]*len(A)
        idx= len(A)-1
        left, right = 0, len(A)-1
        while left<=right:
            if abs(A[left]) > abs(A[right]):
                res[idx] = A[left]**2
                left += 1
            else:
                res[idx] = A[right]**2
                right -=1
            idx -=1
        return res