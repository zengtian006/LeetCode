class Solution:
    def canWin(self, s: str) -> bool:
        dic = {}
        return self.bt(s, dic)
    
    def bt(self, s, dic):
        if s in dic: return dic[s]
        
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                temp = s[:i] + '--' + s[i+2:]
                if not self.canWin(temp):
                    dic[temp] = True
                    return True
        dic[s] = False
        return dic[s]