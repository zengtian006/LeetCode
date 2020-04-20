class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = set(wordDict)
        return self.helper(s, dic, {})
                
    def helper(self, s, dic, visited):
        if s in visited:
            return visited[s]
        if s == '':
            return None
        res = []
        for i in range(len(s)+1):
            if s[:i] in dic:
                rest = self.helper(s[i:], dic, visited)
                if rest == None:
                    res.append(s[:i])
                else:
                    for strr in rest:
                        res.append(s[:i]+' '+strr)
        visited[s] = res
        return visited[s]