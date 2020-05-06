class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, c in enumerate(S):
            last[c] = i
        
        cur_end = cur_start = 0
        res = []
        for i, c in enumerate(S):
            j = last[c]
            cur_end = max(cur_end, j)
            if i == cur_end:
                res.append(i-cur_start+1)
                cur_start = i+1
        return res