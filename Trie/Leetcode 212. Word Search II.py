# Backtracking with Trie
import collections
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word = ''
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.is_word = True
        cur.word = word
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        root = trie.root
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.bt(board, i, j, root, res)
        return res
    
    def bt(self, board, i, j, root, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        val = board[i][j]
        if val not in root.child: # 节枝
            return 
        
        cur = root.child[val]
        if cur.is_word:
            cur.is_word = False
            res.append(cur.word)
        
        board[i][j] = '#'
        self.bt(board, i+1, j, cur, res)
        self.bt(board, i-1, j, cur, res)
        self.bt(board, i, j+1, cur, res)
        self.bt(board, i, j-1, cur, res)
        board[i][j] = val
        


# BackTrakcing(TLE)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word)
        return res
    
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