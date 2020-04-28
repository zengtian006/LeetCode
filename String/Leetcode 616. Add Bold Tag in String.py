class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        n = len(s)
        bold = [False]*n
        end = 0
        res = ""
        for i in range(n):
            for word in dict:
                l = len(word)
                if i+l<=n and s[i:i+l] == word:
                    end = max(end, i+l)
            bold[i] = end>i
            
        i = 0
        while i < n:
            if bold[i] == False:
                res += s[i]
                i += 1
            elif bold[i] == True:
                start = i
                while i<n and bold[i]:
                    i+=1
                res += '<b>'+s[start:i]+'</b>'
        return res