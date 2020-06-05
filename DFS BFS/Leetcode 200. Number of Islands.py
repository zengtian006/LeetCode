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
        res = 0
        dirs = [(1,0),(-1,0), (0,1),(0,-1)]
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res += 1
                    self.helper(grid, i, j, visited)
                    
        return res
    
    def helper(self, grid, x, y,visited):
        m, n = len(grid), len(grid[0])
        if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y] == '1':
            visited.add((x,y))
            self.helper(grid, x+1, y, visited)
            self.helper(grid, x-1, y, visited)
            self.helper(grid, x, y+1, visited)
            self.helper(grid, x, y-1, visited)


    #helper两种写法
    # def helper(self, grid, x, y,visited ):
    #     visited.add((x,y))
    #     dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    #     m, n = len(grid), len(grid[0])
    #     for dx, dy in dirs:
    #         nx = dx + x
    #         ny = dy + y
    #         if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny] == '1':
    #             self.helper(grid, nx, ny, visited)