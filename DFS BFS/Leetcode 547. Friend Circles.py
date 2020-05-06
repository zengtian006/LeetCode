# DFS 
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        visited = [0]*len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                res += 1
                visited[i] = 1
                self.dfs(M, i, visited)
        return res
                            
    def dfs(self, M, i, visited):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, j, visited)

# DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        visited = [0]*len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                res += 1
                stack = []
                stack.append(i)
                while stack:
                    f = stack.pop()
                    for j in range(len(M)):
                        if M[f][j] == 1 and visited[j] == 0:
                            visited[j] = 1
                            stack.append(j)
        return res

# UnionFind
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A
    
    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)
        if root_a == root_b:
            return
        self.parent[root_a] = root_b
        self.count -= 1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        unionFind = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    unionFind.union(i,j)
        return unionFind.count