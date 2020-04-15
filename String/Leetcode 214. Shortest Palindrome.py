class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]
        for i in range(len(s),-1,-1):
            if s[:i] == t[len(s)-i:]:
                break
        return t[:len(s)-i]+s
    
        # s = babcd
        # t = dcbab