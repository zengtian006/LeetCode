class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = collections.deque()
        q.append(1)
        visited = set()
        visited.add(1)
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                num = q.popleft()
                if num == n*n:
                    return step
                for i in range(1,7):
                    if num+i > n*n:
                        break
                    nxt = self.getValue(board, num+i)
                    if nxt == -1:
                        nxt = num+i
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
            step += 1
        return -1
        
        
    def getValue(self, board, num):
        n = len(board)
        x = (num-1)//n
        y = (num-1)%n
        if x%2 == 1:
            y = n-1-y
        x = n-1-x
        return board[x][y]