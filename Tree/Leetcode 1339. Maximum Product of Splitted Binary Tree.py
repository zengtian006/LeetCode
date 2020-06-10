class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.subsums = []
        totalsums = self.helper(root)
        res = 0
        for s in self.subsums:
            res = max(res, s*(totalsums-s))
        return res % (10**9 + 7)
        
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        sums = left+right+root.val
        self.subsums.append(sums)
        return sums 