class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.bt(1, [], k, n, res)
        return res
    
    def bt(self, idx, tempList, k, n, res):
        if n < 0 or k < 0:
            return 
        if n == 0 and k == 0:
            res.append(tempList)
            return
        for i in range(idx,10):
            self.bt(i+1, tempList+[i], k-1, n-i,res)