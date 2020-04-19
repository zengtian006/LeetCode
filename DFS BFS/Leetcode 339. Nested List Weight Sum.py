# BFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        level = 0
        q = collections.deque()
        q.append(nestedList)
        sums = 0
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                nl = q.popleft()
                for n in nl:
                    if n.isInteger():
                        sums += n.getInteger()*level
                    else:
                        q.append(n.getList())
        return sums