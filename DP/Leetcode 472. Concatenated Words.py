class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words)<=2:return []

        dic = set(words)
        res = []
        for word in words:
            if word:
                dic.remove(word)
                dp = [0]*(len(word)+1)
                dp[0] = 1
                for j in range(len(word)+1):
                    for i in range(j):
                        if dp[i] and word[i:j] in dic:
                            dp[j] = 1
                            break
                if dp[-1]: res.append(word)
                dic.add(word)
        return res