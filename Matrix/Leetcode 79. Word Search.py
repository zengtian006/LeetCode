class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        visited = {}
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.bt(board, i, j, 0, word, visited):
                        return True
        return False
    
    def bt(self, board, i, j, idx, word, visited):
        if idx == len(word):
            return True
        
        found = False
        if 0<=i<len(board) and 0<=j<len(board[0]) and not visited.get((i,j)) and board[i][j] == word[idx]:
            visited[(i,j)] = True
            found = self.bt(board, i+1, j, idx+1, word, visited) \
                    or self.bt(board, i-1, j, idx+1, word, visited) \
                    or self.bt(board, i, j+1, idx+1, word, visited) \
                    or self.bt(board, i, j-1, idx+1, word, visited)
            visited[(i,j)] = False
            
        return found