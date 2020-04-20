class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.bt(candidates,0,[],target, res)
        return res
    
    def bt(self, candidates, idx, tempList, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(tempList)
            return 
        for i in range(idx, len(candidates)):
            if i>idx and candidates[i] == candidates[i-1]:
                continue
            self.bt(candidates, i+1, tempList+[candidates[i]], target-candidates[i], res)