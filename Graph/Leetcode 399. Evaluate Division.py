class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = collections.defaultdict(dict)
        for (x,y),r in zip(equations,values):
            dic[x][y] = r
            dic[y][x] = 1/r
            
        res = []
        for m, n in queries:
            if m not in dic:
                res.append(-1)
            else:
                res.append(self.dfs(m, n, dic, set()))
        return res
    
    def dfs(self, m, n, dic, visited):
        if m not in dic:
            return -1
        if m == n:
            return 1
        visited.add(m)
        for nxt in dic[m]:
            if nxt not in visited:
                r = self.dfs(nxt, n, dic, visited)
                if r != -1:
                    return dic[m][nxt]*r
        return -1