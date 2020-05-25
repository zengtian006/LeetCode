# 最短距离，考虑BFS

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings+=1
        min_steps = float('inf')
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    sums = 0
                    visited = set()
                    visited.add((i,j))
                    q = collections.deque()
                    q.append((i,j))
                    step = 0
                    bs = 0
                    while q:
                        size = len(q)
                        step+=1
                        for _ in range(size):
                            x, y = q.popleft()
                            for dx,dy in dirs:
                                nx = dx + x
                                ny = dy + y
                                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                                    if grid[nx][ny] == 1:
                                        sums += step
                                        bs += 1
                                    elif grid[nx][ny] == 0:
                                        q.append((nx,ny))
                                    visited.add((nx,ny))
                    if sums > 0 and bs == buildings:
                        min_steps = min(min_steps, sums)
        return min_steps if min_steps<float('inf') else -1