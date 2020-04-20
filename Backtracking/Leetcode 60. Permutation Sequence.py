# TLE
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res = ''
        self.k = k
        self.bt(n, '', set())
        return self.res
    
    def bt(self, n, strr, visited):
        if len(strr) == n:
            self.k -= 1
            if self.k == 0:
                self.res = strr
                return
        for i in range(1,n+1):
            if self.res:
                break
            if i not in visited:
                visited.add(i)
                self.bt(n, strr+str(i), visited)
                visited.remove(i)