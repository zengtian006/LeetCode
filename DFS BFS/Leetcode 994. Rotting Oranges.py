class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        if not fresh:
            return 0
        q = collections.deque()
        q.extend(rotten)
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        mins = 0
        while q:
            mins += 1
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx = dx + x
                    ny = dy + y
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh-=1
                        if fresh == 0:
                            return mins
                        q.append((nx,ny))
            
        return -1