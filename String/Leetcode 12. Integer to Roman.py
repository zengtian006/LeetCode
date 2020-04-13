class Solution:
    def intToRoman(self, num: int) -> str:
        v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res=""
        for i in range(len(v)):
            while num>=v[i]:
                num -= v[i]
                res += s[i]
        return res