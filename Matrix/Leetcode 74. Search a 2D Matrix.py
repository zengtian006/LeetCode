# Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: 
            return False
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        while top<=bottom:
            mid = top + (bottom - top) //2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        row = top - 1
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

# Two pointer
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        row = 0
        col = len(matrix[0])-1
        while col>=0 and row<len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row+=1
            else: col-=1
        return False