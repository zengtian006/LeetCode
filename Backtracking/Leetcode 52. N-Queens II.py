class Solution:
    def totalNQueens(self, n: int) -> int:
        res = set()
        self.bt(n, 0, [], res)
        return len(res)
    
    def bt(self, n, row, tempList, res):
        if row>n:
            return
        if row==n:
            strr = ''
            for col in tempList:
                strr+=str(col)
            res.add(strr)
        for col in range(n):
            if self.check(col, row, tempList):
                self.bt(n, row+1, tempList+[col],res)
        
    def check(self, col, row, tempList):
        for r in range(row):
            if tempList[r] == col or row-r == abs(tempList[r]-col):
                return False
        return True
    
#     Ex.,
#     [".Q..", 
#      "...Q",
#      "Q...",
#      "..Q."],
    
#     strr = "1403"