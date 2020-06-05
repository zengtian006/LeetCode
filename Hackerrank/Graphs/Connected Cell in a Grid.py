# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

# Complete the maxRegion function below.
def getRegion(grid, x, y, visited):
    m, n = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    res = 1
    for dx, dy in dirs:
        nx = dx + x
        ny = dy + y
        if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny] == 1:
            visited.add((nx,ny))
            res += getRegion(grid, nx, ny, visited)
    return res


def maxRegion(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i,j) not in visited:
                visited.add((i,j))
                region = getRegion(grid, i, j, visited)
                res = max(res, region)
    return res