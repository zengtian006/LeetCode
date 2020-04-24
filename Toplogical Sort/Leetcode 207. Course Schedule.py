class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        child = collections.defaultdict(set)
        parent = collections.defaultdict(int)
        for c, p in prerequisites:
            child[p].add(c)
            parent[c] = parent.get(c,0)+1
        
        q = collections.deque()
        for i in range(numCourses):
            if parent[i] == 0:
                q.append(i)
                del parent[i]
        if not q:
            return False
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for ch in child[course]:
                parent[ch] -=1
                if parent[ch] == 0:
                    q.append(ch)
                    del parent[ch]
        return len(res) == numCourses