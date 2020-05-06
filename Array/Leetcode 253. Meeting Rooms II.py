class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = []
        intervals.sort()
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0]>=rooms[0]:
                heapq.heappop(rooms)
                
            heappush(rooms, interval[1])
        return len(rooms)