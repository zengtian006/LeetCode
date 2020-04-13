class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic= collections.defaultdict(list)
        for strr in strings:
            s = ''
            f = ord(strr[0])
            for c in strr:
                s += str((ord(c) - f)%26)+" "
            print(s)
            dic[s].append(strr)
        res = []
        for v in dic.values():
            res.append(v)
        return res