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



# Differet question. -> Minmum "SPACE" should be added in 's', 相当于 用最少的空格，分隔开字符串s
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = set(wordDict)
        x = self.helper(s, dic, {})
        print(x)
        return x
                
    def helper(self, s, dic, visited):
        if s in visited:
            return visited[s]
        if s == '':
            return 0
        res = float('inf')
        for i in range(len(s)+1):
            if s[:i] in dic:
                rest = self.helper(s[i:], dic, visited)
                if rest != -1:
                    res = min(1+rest, res)
        visited[s] = -1 if res == float('inf') else res
        return visited[s]