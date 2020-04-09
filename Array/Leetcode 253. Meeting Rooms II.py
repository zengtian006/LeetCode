class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        rooms = 0
        j = 0
        for i in range(len(starts)):
            if starts[i] < ends[j]:
                rooms+=1
            else:
                j+=1
        return rooms

# https://www.youtube.com/watch?v=0roQnDBC27o