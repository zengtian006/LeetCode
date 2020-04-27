class UnionFind:
    def __init__(self, n):
        self.parents = [-1]*n
        self.count = 0

    def set_parent(self, i):
        if self.parents[i] != i:
            self.parents[i] = i
            self.count += 1
        
    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i
    
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A != root_B:
            self.parents[root_B] = root_A
            self.count-=1
            
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        unionFind = UnionFind(m*n)
        res = []
        for x, y in positions:
            p = x*n + y
            unionFind.set_parent(p)
            for nx, ny in dirs:
                dx = nx + x
                dy = ny + y
                dp = dx*n+dy
                if 0<=dx<m and 0<=dy<n and unionFind.parents[dp] != -1:
                    unionFind.union(p, dp)
            res += [unionFind.count]
        return res