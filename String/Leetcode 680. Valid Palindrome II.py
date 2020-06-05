class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!=s[right]:
                return self.isValid(s,left+1,right) or self.isValid(s, left, right -1)
            left += 1
            right -=1
        return True
            
    def isValid(self, s, i, j):
        return s[i:j+1] == s[i:j+1][::-1]