class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dic = set(wordDict)
        for j in range(1,len(s)+1):
            for i in range(j):
                if dp[i] == 1 and s[i:j] in dic:
                    dp[j] = 1
        return dp[-1]


# Recursive

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic= set(wordDict)
        visited = {}
        return self.helper(s, dic, visited )
    
    def helper(self, s, dic, visited):
        if s in visited:
            return visited[s]
        if not s:
            return True
        for i in range(len(s)+1):
            if s[:i] in dic:
                if self.helper(s[i:], dic, visited):
                    visited[s] = True
                    return visited[s]
        visited[s] = False
        return False