class Solution1:
    def checkValidString(self, s: str) -> bool:
        dic = {}
        return self.bt(s, 0, 0, dic)
    
    def bt(self, s, idx, sums, dic):
        if sums < 0:
            return False
        key = str(idx) + "+" + str(sums)
        if key in dic:
            return dic[key]
        for i in range(idx, len(s)):
            if s[i] == '(':
                sums += 1
            elif s[i] == ')':
                sums -= 1
                if sums < 0:
                    return False
            elif s[i] == '*':
                dic[key] = self.bt(s, i+1, sums+1, dic) or self.bt(s, i+1, sums-1, dic) or self.bt(s, i+1, sums, dic)
                return dic[key]
        dic[key] = (sums == 0)
        return dic[key]

class Solution2:
    def checkValidString(self, s: str) -> bool:
        stars = []
        opens = []
        for i, char in enumerate(s):
            if char == '(':
                opens.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while stars and opens:
            if stars[-1]>opens[-1]:
                stars.pop()
                opens.pop()
            else:
                break
        return len(opens) == 0