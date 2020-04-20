class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.bt(num, 0, "", 0, target, res)
        return res
    
    def bt(self, num, diff, strr, sums, target, res):
        if sums == target:
            res.append(strr)
            return
        for i in range(1, len(num)+1):
            cur = num[:i]
            if len(cur)>1 and cur[0] == '0':
                return
            rest = num[i:]
            if not strr:
                self.bt(rest, int(cur), cur, int(cur), target, res)
            else:
                # +
                self.bt(rest, int(cur), strr+'+'+cur, sums+int(cur), target, res)
                # -
                self.bt(rest, -int(cur), strr+'-'+cur, sums-int(cur), target, res)
                # *   eg.,: 5-3*2 precal = 5-3, sums = 2, diff = -3. so: 5-3*2 = (2-3)+(-3*2)
                self.bt(rest, diff*int(cur), strr+'*'+cur, (sums-diff)+diff*int(cur), target, res)