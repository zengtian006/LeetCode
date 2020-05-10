class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                temp = s[:i]+'--'+s[i+2:]
                if not self.canWin(temp):
                    return True
        return False
