class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.bt(candidates, 0, [], target, res)
        return res
    
    def bt(self, candidates, idx, tempList, target, res):
        if target < 0:
            return 
        if target == 0:
            res.append(tempList)
            return
        for i in range(idx, len(candidates)):
            self.bt(candidates, i, tempList+[candidates[i]], target-candidates[i], res)