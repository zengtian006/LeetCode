class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] =="1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.helper(heights)    
            res = max(res, area)
        return res
    
    def helper(self, heights):
        res = 0
        n = len(heights)
        if n == 1:
            return heights[0]
        for j in range(n):
            if j == n-1 or heights[j] > heights[j+1]:
                min_height = heights[j]
                for i in range(j,-1,-1):
                    min_height = min(min_height, heights[i])
                    wid = j-i+1
                    area = wid*min_height
                    res = max(res, area)
        return res