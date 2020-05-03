class Solution:
    def searchMatrix(self, matrix, target):
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