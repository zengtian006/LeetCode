class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if interval[1]<newInterval[0]:
                res.append(interval)
            elif interval[0]>newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]            
        res.append(newInterval)
        return res


# interval 问题判断两个条件，一个是能不能插在当前数的后面，另一个是能不鞥插在当前数的前面， 插入在前面的话要记得更新newinteval
# 其他情况就是merge interval
# 最后把newInterval合并到末尾