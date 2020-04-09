class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        pre = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if pre[1]<=interval[0]:
                pre = interval
            else:
                return False
        return True