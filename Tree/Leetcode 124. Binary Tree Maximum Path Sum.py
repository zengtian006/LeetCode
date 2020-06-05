class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return 0
        # 计算左边分支最大值，左边分支如果为负数还不如不选择
        left = max(self.helper(node.left), 0)
        # 计算右边分支最大值，右边分支如果为负数还不如不选择
        right = max(self.helper(node.right), 0)
        self.res = max(self.res, node.val + left + right)
        return max(left, right)+node.val