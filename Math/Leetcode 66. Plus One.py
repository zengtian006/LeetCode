class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            s = digits[i] + carry
            s, carry = s%10, s//10
            res.append(s)
        if carry:
            res.append(carry)
        return res[::-1]