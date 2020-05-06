class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        stack = []
        stack.append(start)
        visited.add((start[0], start[1]))
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx, ny = x, y 
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if [nx, ny] == destination:
                    return True
                if (nx, ny) not in visited:
                    stack.append((nx, ny))
                    visited.add((nx,ny))
        return False