# DFS
class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = collections.defaultdict(set)
        for x,y in edges:
            dic[x].add(y)
            dic[y].add(x)
        
        res = 0
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                res += 1
                self.dfs(dic, visited, i, -1)
        return res
    
    def dfs(self, dic, visited, cur, pre):
        if visited[cur]:
            return
        visited[cur] = 1
        for nxt in dic[cur]:
            if nxt != pre:
                self.dfs(dic, visited, nxt, cur)



# Union Find
class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.components = n
    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB:
            return 
        self.parent[rootA] = rootB
        self.components -= 1
    
class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for A,B in edges:
            unionFind.union(A,B)
        return unionFind.components