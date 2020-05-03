class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        visited = set()
        n = len(matrix)
        h = []
        heapq.heappush(h, (matrix[0][0], 0, 0))
        visited.add((0,0))
        while k>0:
            res, x, y = heapq.heappop(h)
            if x+1 < n and (x+1, y) not in visited:
                heapq.heappush(h, (matrix[x+1][y], x+1, y))
                visited.add((x+1, y))
            if y+1 < n and (x, y+1) not in visited:
                heapq.heappush(h, (matrix[x][y+1], x, y+1))
                visited.add((x, y+1))
            k -= 1
        return res