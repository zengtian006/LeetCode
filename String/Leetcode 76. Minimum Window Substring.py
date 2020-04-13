class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l_s, l_t = len(s), len(t)
        if not s or l_t>l_s:
            return ''
        
        dic = {}
        count = 0
        for char in t:
            dic[char] = dic.get(char,0)+1
        
        l = r = 0
        min_l = l_s + 1
        res = ""
        while r<l_s:
            if s[r] in dic:
                if dic[s[r]] > 0:
                    count += 1
                dic[s[r]] -=1
            
            while count == l_t:
                if r-l+1 < min_l:
                    min_l = r-l+1
                    res = s[l:r+1]
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        count -= 1
                l += 1
            r += 1
        return res