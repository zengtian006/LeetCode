class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word: i for i, word in enumerate(words)}
        res = []
        for word, idx in words.items():
            for i in range(len(word)+1):
                pre = word[:i]
                suf = word[i:]
                if self.isPali(pre):
                    if suf[::-1] in words:
                        if idx != words[suf[::-1]]:
                            res.append([words[suf[::-1]], idx])
                if i !=len(word):
                    if self.isPali(suf):
                        if pre[::-1] in words:
                            if idx != words[pre[::-1]]:
                                res.append([idx, words[pre[::-1]]])

        return res
    
    def isPali(self, strr):
        return strr[::-1] == strr