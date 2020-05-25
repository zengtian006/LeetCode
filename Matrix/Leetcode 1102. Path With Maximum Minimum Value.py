from heapq import *
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A),len(A[0])
        visited = [[0]*n for _ in range(m)]
        q=[]
        heappush(q,(-A[0][0],0,0))
        visited[0][0] = 1
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        res = float('inf')
        while q:
            v,x,y = heappop(q)
            res = min(res,-v)
            if x == m-1 and y == n-1:
                return res
            for xd,yd in dirs:
                nx = x + xd
                ny = y + yd
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    heappush(q,(-A[nx][ny],nx,ny))
                    visited[nx][ny] = 1