class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.dic = collections.defaultdict(list)
        for u,v in connections:
            self.dic[u].append(v)
            self.dic[v].append(u)
        self.ids = [0]*n
        self.low = [0]*n
        visited = [0]*n        
        idx = 0
        self.res = []
        self.dfs(0, None, idx, visited)
        
        # print(self.low)
        # print(self.ids)
        return self.res
        
    def dfs(self, cur, par, idx, visited):
        visited[cur] = 1
        self.ids[cur] = self.low[cur] = idx
        for nxt in self.dic[cur]:
            if nxt == par:
                continue
            if not visited[nxt]:
                self.dfs(nxt, cur, idx+1, visited)
                self.low[cur] = min(self.low[cur], self.low[nxt])
                if self.low[nxt]>self.ids[cur]:
                    self.res.append([cur, nxt])
            elif visited[nxt]:
                self.low[cur] = min(self.low[cur], self.low[nxt])
        
                