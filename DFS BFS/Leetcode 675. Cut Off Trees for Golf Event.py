class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        res = 0
        s1 = s2 = 0
        while heap:
            tree, x, y = heapq.heappop(heap)
            count = self.bfs(forest, s1, s2, x, y)
            if count == -1:
                return -1
            res += count
            s1 = x
            s2 = y
        return res
    
    def bfs(self, forest, s1,s2,e1,e2):
        if s1 == e1 and s2 == e2:
            return 0
        visited = set()
        m, n = len(forest), len(forest[0])
        count = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        q = collections.deque()
        visited.add((s1,s2))
        q.append((s1,s2))
        while q:
            size = len(q)
            count+=1
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx = dx + x
                    ny = dy + y
                    if nx == e1 and ny == e2:
                        return count
                    if 0<=nx<m and 0<=ny<n and forest[nx][ny] != 0 and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
        return -1