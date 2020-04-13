class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = {}
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] not in dic:
                k -= 1
            dic[s[j]] = dic.get(s[j], 0) + 1
            
            if k > -1:
                res = max(res, j-i+1)
            while k == -1:
                if s[i] in dic:
                    dic[s[i]] -= 1
                    if dic[s[i]] == 0:
                        k +=1
                        del dic[s[i]]
                i += 1
        return res