class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right= self.dfs(node.right)
        self.res = max(self.res, left + right + node.val)
        cur_max = max(left, right) + node.val
        return max(cur_max, 0)