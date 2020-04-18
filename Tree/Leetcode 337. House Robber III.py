class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        dic = {}
        self.dfs(root, dic)
        return self.res
    def dfs(self, node, dic):
        if not node:
            return 0
        if node in dic:
            return dic[node]
        left = self.dfs(node.left, dic)
        right = self.dfs(node.right, dic)
        v = node.val
        if node.left:
            v += self.dfs(node.left.left, dic) + self.dfs(node.left.right, dic)
        if node.right:
            v += self.dfs(node.right.left, dic) + self.dfs(node.right.right, dic)
        dic[node] = self.res = max(v, left+right)
        return dic[node]