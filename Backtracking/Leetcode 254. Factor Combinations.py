class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <=1:
            return[]
        res = []
        self.bt(n, 2, [], res)
        return res
    
    def bt(self, n, idx, tempList, res):
        if len(tempList)>1 and n == 1:
            res.append(tempList)
            return 
        for i in range(idx,n+1):
            if n%i ==0:
                self.bt(n//i, i, tempList+[i], res)