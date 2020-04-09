class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        res = []
        intervals.sort()
        pre = intervals[0]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] > pre[1]:
                res.append(pre)
                pre = interval
            elif interval[1] < pre[0]:
                res.append(interval)
            else:
                pre = [min(interval[0],pre[0]),max(interval[1],pre[1])]
        res.append(pre)
        return res