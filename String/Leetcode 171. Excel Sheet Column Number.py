class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            n = ord(char) - ord('A') +1
            res = res*26 +n
        return res