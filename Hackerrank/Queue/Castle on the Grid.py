# https://www.hackerrank.com/challenges/castle-on-the-grid/problem
import collections
def minimumMoves(grid, startX, startY, goalX, goalY):
    m, n = len(grid), len(grid[0])
    q = collections.deque()
    q.append((startX, startY))
    visited = set()
    visited.add((startX, startY))
    step = 0
    dirs = [(0,1),(1,0),(-1,0), (0,-1)]
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in dirs:
                nx = x
                ny = y
                while 0<=nx<m and 0<=ny<n and grid[nx][ny] != 'X':
                    if (nx,ny) == (goalX, goalY):
                        return step+1
                    nx += dx
                    ny += dy
                    if (nx,ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx,ny))
        step+=1
    return -1