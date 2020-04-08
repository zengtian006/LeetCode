import collections
class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = collections.defaultdict(set)
        for i in range(len(words)):
            self.dic[words[i]].add(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        for i in self.dic[word1]:
            for j in self.dic[word2]:
                res = min(res, abs(i-j))
        return res