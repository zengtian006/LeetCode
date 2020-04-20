class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.bt(0, '', digits, dic, res)
        return res
    
    def bt(self, idx, strr, digits, dic ,res):   
        if len(strr) == len(digits):
            res.append(strr)
            return
        for i in range(idx, len(digits)):
            for char in dic[digits[i]]:
                self.bt(i+1, strr+char, digits, dic, res)