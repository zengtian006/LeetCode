class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = 0
        for s in S:
            if s != '#':
                S = S[:i]+s+S[i+1:]
                i+=1
            else:
                if i>0:
                    i-=1
        j = 0
        for t in T:
            if t != '#':
                T = T[:j]+t+T[j+1:]
                j+=1
            else:
                if j>0:
                    j-=1
        return S[:i] == T[:j]