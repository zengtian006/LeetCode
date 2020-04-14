import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = collections.deque([s])
        res = []
        visited = set()
        visited.add(s)
        found = False
        while q:
            strr = q.popleft()
            if self.isValid(strr):
                res.append(strr)
                found = True
            if found:
                continue
            for i in range(len(strr)):
                if strr[i] in '()':
                    s = strr[:i]+strr[i+1:]
                    if s not in visited:
                        q.append(s)
                        visited.add(s)
        return res
    
       
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count+=1
            elif c == ')':
                count-=1
            if count<0:
                return False
        return count == 0


# 求所有的可能，考虑BFS， DFS， Backtracking， Divid and Conqure