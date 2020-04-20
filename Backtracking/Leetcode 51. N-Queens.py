class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.bt(n, 0, [], res)
        return res
    
    def bt(self, n, row, tempList, res):
        if row == n:
            s = ''
            r = []
            for x in tempList:
                s = "."*x + 'Q' + "."*(n-x-1)
                r.append(s)
            res.append(r)
            return
        for j in range(n):
            if self.check(row,j,tempList):
                self.bt(n, row+1, tempList+[j], res)
                    
    def check(self, row, col, tempList):
        for i in range(len(tempList)):
            if abs(i-row) == abs(tempList[i] - col) or col == tempList[i]:
                return False
        return True