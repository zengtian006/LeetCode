#TLE

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        person = []
        visited= set()
        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    person.append((i,j))
                    visited.add((i,j))
                    
        for i, j in person:
            steps = 0
            q = collections.deque()
            q.append((i,j))
            v = set()
            v.add((i,j))
            while q:
                size = len(q)
                steps+=1
                for _ in range(size):
                    x, y = q.popleft()
                    for dx,dy in dirs:
                        nx = dx + x
                        ny = dy + y
                        if 0<=nx<m and 0<=ny<n and (nx,ny) not in v:
                            grid[nx][ny] += steps
                            v.add((nx,ny))
                            q.append((nx,ny))
        res = float('inf')
        for i in range(m):
            for j in range(n):
                res = min(res, grid[i][j])
        return res if res<float('inf') else 1