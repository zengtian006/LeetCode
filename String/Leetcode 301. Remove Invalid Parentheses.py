# 求所有的可能，考虑BFS， DFS， Backtracking， Divid and Conqure
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




# Backtracking
class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited = set()
        self.ml = -1
        self.lens = collections.defaultdict(set)
        self.helper(s, visited)
        return list(self.lens[self.ml])
    
    def helper(self, s, visited):
        if s in visited:
            return
        if self.isValid(s):
            if len(s) >= self.ml:
                self.ml = len(s)
                self.lens[len(s)].add(s)
        visited.add(s)
        for i in range(len(s)):
            if s[i] in '()':
                ss = s[:i] + s[i+1:]
                if ss not in visited:
                    self.helper(ss,visited)
            
            
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count +=1
            elif c==')':
                count -=1
            if count < 0 :
                return False
        return count == 0