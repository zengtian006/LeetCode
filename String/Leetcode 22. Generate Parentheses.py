class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, '', n, n)
        return res
    
    def helper(self, res, tempList, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(tempList)
        if left>0:
            self.helper(res,tempList+'(', left-1,right)
        if right>0:
            self.helper(res, tempList+')', left, right-1)