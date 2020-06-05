class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for t in tasks:
            dic[t] = dic.get(t, 0) +1
        heap = []
        for count in dic.values():
            heapq.heappush(heap, -count)
        res = 0
        
        while heap:
            temp = []
            i =0 
            while i<=n:
                res += 1
                if heap:
                    cnt = heapq.heappop(heap)
                    if cnt != -1:
                        temp.append(cnt+1)
                if not heap and not temp:
                    break # finish all tasks
                else:
                    i+=1
            for t in temp:
                heapq.heappush(heap, t)
        return res