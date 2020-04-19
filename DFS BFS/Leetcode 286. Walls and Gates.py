# DFS
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        stack = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    stack.append((i,j))
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx = dx + x
                ny = dy + y
                if 0<=nx<m and 0<=ny<n and rooms[nx][ny]!=-1 and rooms[x][y] + 1 < rooms[nx][ny]:
                    rooms[nx][ny] = rooms[x][y] + 1
                    stack.append((nx,ny))

# BFS
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy                                
                if 0<=nx<m and 0<=ny<n and rooms[nx][ny] == 2147483647 and rooms[x][y]<rooms[nx][ny]+1: 
                    rooms[nx][ny] = rooms[x][y]+1
                    q.append((nx,ny))