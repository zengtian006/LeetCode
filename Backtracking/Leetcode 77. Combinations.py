class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.bt(n, 1, [], k, res)
        return res

    def bt(self, n, idx, tempList, k, res):
        if len(tempList) == k:
            res.append(tempList)
            return
        for i in range(idx, n+1):
            self.bt(n, i+1, tempList + [i], k, res)