import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for l,r,h in buildings:
            points.append([l, h, 'start'])
            points.append([r, -h, 'end'])
        points.sort(key=lambda x:( x[0], -x[1]))
        # start before end; start: lowest first, end: highest first
        print(points)
        res, max_heap= [], [0]
        for point in points:
            if point[2] == 'start':
                if point[1]>-max_heap[0]:
                    res.append([point[0],point[1]])
                heapq.heappush(max_heap, -point[1])
            elif point[2] == 'end':
                max_heap.remove(point[1])
                heapq.heapify(max_heap)
                if -point[1]>-max_heap[0]:
                    res.append([point[0], -max_heap[0]])
        return res
        

# 想象有一条竖线从左到右扫描，start：左上角 每次选出当前最高的点；如果是 end：右上角，将同样高度的左上角删除，重新排列后，如果最高点不变，则继续扫描，否则，选出当前最高的点，