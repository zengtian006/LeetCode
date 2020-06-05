class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dic_p = {}
        for char in p:
            dic_p[char] = dic_p.get(char,0)+1
        
        dic_s = {}
        i = 0
        for j in range(len(s)):
            dic_s[s[j]] = dic_s.get(s[j],0)+1
            
            if j>=len(p):
                dic_s[s[i]] -= 1
                i+=1
            if self.equal(dic_s, dic_p):
                res.append(i)
        return res
    
    def equal(self, a,b):
        for k in a.keys():
            if a.get(k,0)!=b.get(k,0):
                return False
        for k in b.keys():
            if a.get(k,0)!=b.get(k,0):
                return False
        return True