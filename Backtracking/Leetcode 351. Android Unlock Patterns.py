class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.m, self.n = m, n
        res = []
        self.bt(1, [], res)
        return len(res)
    
    def bt(self, start, tempList, res):
        checkPairs = [(1,3),(3,1),(1,7),(7,1),(1,9),(9,1),(2,8),(8,2),(3,7),(7,3),(3,9),(9,3),(4,6),(6,4),(7,9),(9,7)]
        if self.m<=len(tempList)<=self.n:
            res.append(tempList)
        for i in range(1, 10):
            if i in tempList:
                continue
            if len(tempList)==self.n:
                break
            if len(tempList)>=1:
                if (i,tempList[-1]) in checkPairs and (i + tempList[-1]) // 2 not in tempList:
                    continue
            self.bt(i+1, tempList+[i],res)
    