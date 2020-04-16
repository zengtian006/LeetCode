class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        m,n = len(a)-1,len(b)-1
        res = ''
        while m>=0 or n>=0:
            s = 0
            if m >=0:
                s += int(a[m])
                m-=1
            if n >=0:
                s+=int(b[n])
                n-=1
            s += carry
            s, carry = s%2, s//2
            res = str(s) + res
        if carry:
            res = str(carry) + res
        return res