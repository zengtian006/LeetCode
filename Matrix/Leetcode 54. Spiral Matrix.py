class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return 
        m, n = len(matrix), len(matrix[0])
        res = []
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        while top<bottom and left<right:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            
            top+=1
            bottom -=1
            left += 1
            right -= 1
        if top == bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        elif left == right:
            for i in range(top, bottom+1):
                res.append(matrix[i][left])
        return res