class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return []
        res = []
        self.helper(s, [], res)
        return res
    
    
    def helper(self, s, tempList, res):
        if len(tempList) == 4 and not s:
            res.append(".".join(tempList))
            return
        if len(tempList)>4:
            return

        for i in range(1,min(4,len(s)+1)):
            if i>1 and s[0]=='0':
                break
            if 0<=int(s[:i])<=255:
                self.helper(s[i:], tempList+[s[:i]], res)