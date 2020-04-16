class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1),len(num2)
        offset = 0
        res = [0]*(m+n)
        for i in range(n-1,-1,-1):
            self.mul(int(num2[i]), num1, offset, res)
            offset += 1
        result = 0
        for i in range(len(res)):
            result = result*10 + res[i]
        return str(result)
    
    def mul(self, mul, nums, offset, res):
        carry = 0
        j = len(res)-1
        for i in range(len(nums)-1,-1,-1):
            s = mul * int(nums[i]) + carry + res[j-offset]
            s, carry = s%10, s//10
            res[j-offset] = s
            j -= 1
        if carry>0:
            res[j-offset] = carry