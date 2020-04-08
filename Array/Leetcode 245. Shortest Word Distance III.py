import collections
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        dic = collections.defaultdict(set)
        for i in range(len(words)):
            dic[words[i]].add(i)
            
        res = float('inf')
        for i in dic[word1]:
            for j in dic[word2]:
                if i!=j:
                    res = min(res, abs(i-j))
        return res