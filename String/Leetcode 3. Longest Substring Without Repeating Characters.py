class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        dic = {}
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]]+1, i)
            dic[s[j]] = j
            res = max(res, j-i+1)
        return res