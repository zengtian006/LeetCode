class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for x,y in zip(s,t):
            if x not in dic1:
                dic1[x] = y
            if y not in dic2:
                dic2[y] = x
            if dic1[x]!=y or dic2[y]!=x:
                return False
        return True