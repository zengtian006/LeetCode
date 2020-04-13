class Solution:
    def romanToInt(self, s: str) -> int:
        ss = ["I","V","X","L","C","D","M"]
        vv = [1,5,10,50,100,500,1000]
        dic = {}
        for k,v in zip(ss,vv):
            dic[k]=v
        res = dic[s[0]]
        for i in range(1,len(s)):
            if dic[s[i]]>dic[s[i-1]]:
                res += dic[s[i]]-dic[s[i-1]]*2
            else:
                res += dic[s[i]]
        return res