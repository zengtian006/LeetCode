import collections
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = collections.defaultdict(set)
        for i in range(len(words)):
            for ch in words[i]:
                dic[i].add(ch)
        
        res = 0
        for i in range(1,len(words)):
            for j in range(i):
                if not (dic[i] & dic[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res