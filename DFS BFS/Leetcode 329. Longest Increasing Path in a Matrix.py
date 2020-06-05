class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        visited = {}
        res = 0
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, i, j, visited)
                res = max(res, path)
        return res
    
    def dfs(self, matrix, x, y, visited):
        m, n = len(matrix), len(matrix[0])
        if (x,y) in visited:
            return visited[(x,y)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 1
        for dx, dy in dirs:
            nx = dx + x
            ny = dy + y
            if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>matrix[x][y]:
                res = max(res, 1 + self.dfs(matrix, nx, ny, visited))
        visited[(x,y)] = res
        return res