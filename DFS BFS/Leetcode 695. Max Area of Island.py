class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = []
                    stack.append((i,j))
                    grid[i][j] = '#'
                    cur_area = 1
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in dirs:
                            nx = dx + x
                            ny = dy + y
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                                cur_area += 1
                                stack.append((nx,ny))
                                grid[nx][ny] = '#'
                    res = max(res, cur_area)
        return res