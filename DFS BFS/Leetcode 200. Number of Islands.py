# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    stack = [(i,j)]
                    grid[i][j] = '#'
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in dirs:
                            nx = dx + x
                            ny = dy + y
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == '1':
                                stack.append((nx,ny))
                                grid[nx][ny] = '#'
        return res


# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        res = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    q.append((i,j))
                    grid[i][j] = "#"
                    while q:
                        x, y = q.popleft()
                        for dx, dy in dirs:
                            nx = x + dx
                            ny = y + dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                                q.append((nx,ny))
                                grid[nx][ny]="#"
        return res


# Recursive
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(grid, i, j)
        return res
    def helper(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if 0<=i<m and 0<=j<n and grid[i][j] == '1':
            grid[i][j] = '#'
            self.helper(grid, i+1, j)
            self.helper(grid, i-1, j)
            self.helper(grid, i, j+1)
            self.helper(grid, i, j-1)