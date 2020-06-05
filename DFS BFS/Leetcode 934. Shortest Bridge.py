class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A),len(A[0])
        i,j = self.getFirst(A)
        
        visited = set()
        self.helper(A, i, j, visited)
           
        res = float('inf')
        lst = []
        lst.extend(visited)

        for (i, j) in lst:
            dst = self.getDst(A, i, j, visited)
            if dst:
                res = min(res, dst)
        return res
    
    def getFirst(self, A):
        m, n = len(A),len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    return i, j
                
    def getDst(self, A, i, j, visited):
        m, n = len(A),len(A[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        
        q = collections.deque()
        q.append((i,j))
        visited2 = set()
        visited2.add((i,j))
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx = dx + x
                    ny = dy + y 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                        if A[nx][ny] == 1:
                            return step
                        if (nx,ny) not in visited2 and A[nx][ny] == 0:
                            q.append((nx,ny))
                            visited2.add((nx,ny))
            step +=1 
     
    def helper(self, A, x, y, visited):
        visited.add((x,y))
        m, n = len(A),len(A[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        for dx, dy in dirs:
            nx = dx + x
            ny = dy + y 
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and A[nx][ny] == 1:
                self.helper(A, nx, ny, visited)