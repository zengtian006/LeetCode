class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        v1 = [[0]*n for _ in range(m)] # left to right
        v2 = [[0]*n for _ in range(m)] # right to left
        v3 = [[0]*n for _ in range(m)] # top to bottom 
        v4 = [[0]*n for _ in range(m)] # bottom to top
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'E':
                    v1[i][j] = (v1[i][j-1] if j>0 else 0) + 1
                elif grid[i][j] == 'W':
                    v1[i][j] = 0
                else:
                    v1[i][j] = v1[i][j-1] if j>0 else 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 'E':
                     v2[i][j] = (v2[i][j+1] if j<n-1 else 0) + 1
                elif grid[i][j] == 'W':
                     v2[i][j] = 0
                else:
                    v2[i][j] = v2[i][j+1] if j<n-1 else 0
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 'E':
                    v3[i][j] = (v3[i-1][j] if i > 0 else 0) + 1
                elif grid[i][j] == 'W':
                    v3[i][j] = 0
                else:
                    v3[i][j] = (v3[i-1][j] if i > 0 else 0)
            for i in range(m-1, -1,-1):
                if grid[i][j] == 'E':
                    v4[i][j] = (v4[i+1][j] if i < m-1 else 0) + 1
                elif grid[i][j] == 'W':
                    v4[i][j] = 0
                else:
                    v4[i][j] = (v4[i+1][j] if i < m-1 else 0)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, v1[i][j]+ v2[i][j]+ v3[i][j]+ v4[i][j])
        return res