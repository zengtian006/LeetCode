class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res-1
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left+right+1)
        return max(left, right) +1