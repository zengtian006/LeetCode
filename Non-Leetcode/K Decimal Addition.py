# Example1

# Input: k = 3, a = "12", b = "1"
# Output: 20
# Explanation: 
# 12 + 1 = 20 in 3 bases.
# Example2

# Input: k = 10, a = "12", b = "1"
# Output: 13
# Explanation: 
# 12 + 1 = 13 in 10 bases.


# 先转成10进制，再转回k进制
class Solution:
    def addition(self, k, a, b):
        # Write your code here
        a = self.to_ten(a,k)
        b = self.to_ten(b,k)
        sums = a+b
        res = ''
        while sums > 0:
            sums, n = divmod(sums, k)
            res = str(n)+res
        return res
            
            
    def to_ten(self, a, k):
        r = 0
        total = 0
        for i in range(len(a)-1,-1,-1):
            total += int(a[i])*(k**r)
            r+=1
        return total