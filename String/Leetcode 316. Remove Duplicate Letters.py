class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for char in s:
            dic[char] = dic.get(char,0)+1
        res = []
        for char in s:
            dic[char] -= 1
            if char not in res:
                while res and char<res[-1] and dic[res[-1]]>0:
                    res.pop()
                res.append(char)
        return ''.join(res)