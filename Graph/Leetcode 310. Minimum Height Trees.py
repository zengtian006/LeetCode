import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dic = collections.defaultdict(set)
        for x,y in edges:
            dic[x].add(y)
            dic[y].add(x)
        
        q = collections.deque()
        res = []
        for i in range(n):
            if len(dic[i]) == 1: #leaf node
                q.append(i)
        while n > 2:
            l = len(q)
            n -= l
            for i in range(l):
                node = q.popleft()
                for nxt in dic[node]:
                    dic[nxt].remove(node)
                    if len(dic[nxt]) == 1:
                        q.append(nxt)
        while q:
            res.append(q.popleft())
        return res