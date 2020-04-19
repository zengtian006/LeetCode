class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        dic = {}
        level = 0
        q = collections.deque()
        q.append(nestedList)
        res = 0
        while q:
            size = len(q)
            level += 1
            sums = 0
            for _ in range(size):
                nl = q.popleft()
                for n in nl:
                    if n.isInteger():
                        sums += n.getInteger()
                    else:
                        q.append(n.getList())
            dic[level] = sums
                
        for k, v in dic.items():
            res += (level+1-k)*v
        return res