class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    x = self.helper(grid, i, j, visited)
                    res = max(res, x)
        return res
    
    
    def helper(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        res = 0
        if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y]!=0:
            visited.add((x,y))
            res = grid[x][y] + max(self.helper(grid, x-1,y,visited), self.helper(grid, x,y-1,visited), self.helper(grid, x+1,y,visited), self.helper(grid, x,y+1,visited))
            visited.remove((x,y))
        return res