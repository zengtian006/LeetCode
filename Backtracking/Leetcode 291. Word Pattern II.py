class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.bt(pattern, 0, str, 0, {})
    
    def bt(self, pattern, p, strr, r, dic):
        if p == len(pattern) and r == len(strr):
            return True
        if p == len(pattern) or r == len(strr):
            return False
        
        char = pattern[p]
        for i in range(r, len(strr)):
            s = strr[r:i+1]
            if char in dic and dic[char] == s:
                if self.bt(pattern, p+1, strr, i+1, dic):
                    return True
            elif char not in dic:
                b = False
                for v in dic.values():
                    if v == s:
                        b = True
                if not b:
                    dic[char] = s
                    if self.bt(pattern, p+1, strr, i+1, dic):
                        return True
                    del dic[char]
        return False