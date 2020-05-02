class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        top = left = 0
        bottom = right = n-1
        x = 1
        while top<bottom:
            for i in range(left, right):
                res[top][i] = x
                x += 1
            for i in range(top, bottom):
                res[i][right] = x
                x += 1
            for i in range(right, left, -1):
                res[bottom][i] = x
                x += 1
            for i in range(bottom, top, -1):
                res[i][left] = x
                x += 1
            top += 1
            left += 1
            bottom -= 1
            right -= 1
            
        if top == bottom:
            res[top][left] = x
        return res
            