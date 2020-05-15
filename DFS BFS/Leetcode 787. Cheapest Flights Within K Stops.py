# DFS
# 时间复杂度 O(K*E)  E代表有多少条边(航线)，最坏情况每条边遍历K次
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(dict)
        for s,d,c in flights:
            dic[s][d] = c
        visited = [0]*n
        self.res = float('inf')
        visited[src] = 1
        self.helper(dic, src, dst, K+1, 0, visited)
        return self.res if self.res<float('inf') else -1
    
    def helper(self ,dic ,src ,dst, k, cost, visited):
        if src == dst:
            self.res = cost
            return 
        if k ==0:
            return 
        for v, e in dic[src].items():
            if visited[v]:
                continue
            if e+cost>self.res: # 最关键的一步，不然后面大于self.res会把之前的self.res覆盖掉
                continue
            visited[v] = 1
            self.helper(dic, v, dst, k-1, cost+e, visited)
            visited[v] = 0

# BFS
# 时间复杂度 O(n*(K+1))
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(dict)
        for s,d,c in flights:
            dic[s][d] = c
        visited = [0]*n
        res = float('inf')
        q = collections.deque()
        k = K+1
        q.append((src, 0))
        while q:
            size = len(q)
            for _ in range(size):
                cur, cost = q.popleft()
                if cur == dst:
                    res = min(res, cost)
                for v, w in dic[cur].items():
                    if w+cost > res:
                        continue
                    q.append((v, w+cost))
            k-=1
            if k == -1:
                break
        return res if res<float('inf') else -1