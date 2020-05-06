class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = {}
        heap = []
        heapq.heappush(heap, (0, start[0],start[1]))
        visited[(start[0], start[1])] = 0
        res = m*n
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        while heap:
            step, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                count = 0
                nx, ny = dx+x, dy+y 
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                    count += 1
                nx -= dx
                ny -= dy
                if [nx, ny] == destination:
                    return step+count
                if (nx, ny) not in visited or step+count < visited[(nx,ny)]:
                    heapq.heappush(heap, (step+count, nx,ny))
                    visited[(nx,ny)] = step+count
        return -1