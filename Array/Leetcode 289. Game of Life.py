class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 0 -> 0 status = 0
        # 1 -> 1 status = 1
        # 1 -> 0 status = 2
        # 0 -> 1 status = 3
        m, n = len(board), len(board[0])
        directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        for x in range(m):
            for y in range(n):
                lives = 0
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<m and 0<=ny<n and (board[nx][ny] == 1 or board[nx][ny] == 2) :
                        lives+=1

                if board[x][y] == 0 and lives==3: # rule 4
                    board[x][y] = 3
                elif board[x][y] == 1 and (lives<2 or lives>3):
                    board[x][y] = 2
        for x in range(m):
            for y in range(n):
                board[x][y] = board[x][y]%2
        return board