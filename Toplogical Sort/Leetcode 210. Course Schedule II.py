class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        child = collections.defaultdict(set)
        parent = collections.defaultdict(int)
        for c, p in prerequisites:
            child[p].add(c)
            parent[c] +=1
        
        q = collections.deque()
        for i in range(numCourses):
            if parent[i] == 0:
                q.append(i)
                del parent[i]
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for ch in child[course]:
                parent[ch] -= 1
                if parent[ch] == 0:
                    q.append(ch)
                    del parent[ch]
        return res if len(res) == numCourses else []