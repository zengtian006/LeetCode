# DFS
class Solution1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = collections.defaultdict(set)
        for x,y in edges:
            dic[x].add(y)
            dic[y].add(x)
        
        visited = [0]*n
        if not self.dfs(dic, visited, 0, -1):
            return False
        for v in visited:
            if v == 0:
                return False
        return True
        
        
    def dfs(self, dic, visited, cur, pre):
        if visited[cur]:
            return False
        visited[cur] = 1
        for nxt in dic[cur]:
            if nxt!=pre:
                if not self.dfs(dic, visited, nxt, cur):
                    return False
        return True


# Union Find
class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB:
            return False
        self.parent[rootA] = rootB
        return True


class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        unionFind = UnionFind(n)
        for A, B in edges:
            if not unionFind.union(A,B):
                return False
        return True


# Union find 是解决图的连通性，Find方法是寻找该点是属于哪个集合， 
# 如果A，B 分属于不同集合，就将这两个元素所在的集合合并放在一个集合里面（Union方法）
# 如果A，B属于同一个集合，则该集合有环