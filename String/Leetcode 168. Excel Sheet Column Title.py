class Solution1:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n>26:
            n,m = divmod(n, 26)
            if m ==0:
                m = 26
                n -= 1
            res = chr(m-1 + ord('A')) + res
        res = chr(n-1+ord('A')) + res
        return res
            
        
class Solution2:
    def convertToTitle(self, n: int) -> str:        
        if n<=26:
            return chr(ord('A')+ n-1)
        else:
            return self.convertToTitle((n-1)//26)+chr((n-1)%26+ord('A'))