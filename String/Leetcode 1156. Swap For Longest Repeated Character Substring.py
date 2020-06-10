class Solution:
    def maxRepOpt1(self, text: str) -> int:
        group = []
        dic = {}
        i = 0
        while i < len(text):
            char = text[i]
            count = 0
            while i< len(text) and text[i] == char:
                count += 1
                i+=1
            group.append((char,count))
            dic[char] = dic.get(char, 0)+count
        
        res = 0
        for i in range(len(group)):
            (k, count) = group[i]
            res = max(res, min(count+1, dic[k]))
        for i in range(1, len(group)-1):
            if group[i-1][0] == group[i+1][0] and group[i][1] == 1:
                count = min(group[i-1][1] + group[i+1][1] +1, dic[group[i-1][0]])
                res = max(res, count)
        return res