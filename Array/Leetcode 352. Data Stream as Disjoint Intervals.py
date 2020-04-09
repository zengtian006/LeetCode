class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        res = []
        newInterval = [val, val]
        for i in range(len(self.intervals)):
            interval = self.intervals[i]
            if newInterval[1] < interval[0]-1:
                res.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]+1:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)
        self.intervals = res

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# 与Leetcode57 基本一样