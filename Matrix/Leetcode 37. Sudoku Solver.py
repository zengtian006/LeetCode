class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] !='.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 +j//3].add(num)
        self.bt(board, 0 ,0, rows, cols, boxes)
        
    def bt(self, board, i, j, rows, cols, boxes):
        if i == 9: return True
        if j >=9: return self.bt(board, i+1, 0, rows, cols, boxes)
        if board[i][j] != '.':
            return self.bt(board, i, j+1, rows, cols, boxes)
        
        for k in range(1,10):
            if self.isValid(board, i, j, k, rows, cols, boxes):
                board[i][j] = str(k)
                rows[i].add(k)
                cols[j].add(k)
                boxes[(i//3)*3 +j//3].add(k)
                if self.bt(board, i, j+1, rows, cols, boxes):
                    return True
                rows[i].remove(k)
                cols[j].remove(k)
                boxes[(i//3)*3 +j//3].remove(k)
                board[i][j] = '.'

        return False
    
    def isValid(self, board, x, y, v, rows, cols, boxes):
        if v in rows[x] or v in cols[y] or v in boxes[(x//3)*3+y//3]:
            return False
        return True