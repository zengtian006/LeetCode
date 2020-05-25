class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                graph[j].append(i)
        visited = set()
        q = collections.deque()
        q.append(S)
        res = 0
        while q:
            size = len(q)
            res +=1
            for _ in range(size):
                station = q.popleft()
                for route in graph[station]:
                    if route in visited:
                        continue
                    visited.add(route)
                    for nxt_station in routes[route]:
                        if nxt_station == T:
                            return res
                        if nxt_station!=station:
                            q.append(nxt_station)
        return -1


# https://www.cnblogs.com/grandyang/p/10293947.html