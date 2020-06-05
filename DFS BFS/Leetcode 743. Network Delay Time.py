class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s,d,w in times:
            graph[s][d] = w
            
        q = [(0,K)]
        dist = [float('inf')]*(N+1)
        dist[K] = 0
        while q:
            cost, node = heapq.heappop(q)
            for nxt in graph[node]:
                newCost = cost + graph[node][nxt]
                if dist[nxt] > newCost:
                    dist[nxt] = newCost
                    heapq.heappush(q, (newCost, nxt))
        return -1 if max(dist[1:]) == float('inf') else max(dist[1:])