class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps == 0 or arrLen == 1:
            return 1
            
        visited = {}
        return self.helper(0, steps, arrLen, visited) % (10 ** 9 + 7)
    
    def helper(self, pos, steps, n, visited):
        if (pos, steps) in visited:
            return visited[(pos, steps)]
        if steps == 0:
            if pos == 0:
                return 1
            else:
                return 0
        if pos > steps:
            return 0
        res = self.helper(pos, steps-1, n, visited)
        if 0<=pos+1<n:
            res += self.helper(pos+1, steps-1, n, visited)
        if 0<=pos-1<n:
            res += self.helper(pos-1, steps-1, n, visited) 
        visited[(pos, steps)] = res
        return visited[(pos, steps)]