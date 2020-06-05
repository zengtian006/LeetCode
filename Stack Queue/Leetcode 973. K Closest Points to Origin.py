import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = []
        p_arr = []
        for i in range(len(points)):
            point = points[i]
            d=(point[0]**2 + point[1]**2)**0.5
            p_arr.append((d,i))
            
        h = []
        for i in range(len(p_arr)):
            if i<K:
                heapq.heappush(h, (-p_arr[i][0],p_arr[i][1]))
            else:
                if -p_arr[i][0]>h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (-p_arr[i][0],p_arr[i][1]))
        res = []
        while h:
            res.append(points[heapq.heappop(h)[1]])
        return res