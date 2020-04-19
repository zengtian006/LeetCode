# DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        stack = []
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    board[i][j] = '#'
                    stack.append((i,j))
        while stack:
            x,y = stack.pop()
            for dx,dy in dirs:
                nx = dx + x
                ny = dy + y
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == 'O':
                    stack.append((nx,ny))
                    board[nx][ny] = '#'
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'