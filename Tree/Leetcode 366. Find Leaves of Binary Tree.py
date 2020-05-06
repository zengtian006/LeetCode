class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        self.dfs(d, root)
        res = []
        for v in d.values():
            res.append(v)
        return res
        
    def dfs(self, d, node):
        if not node:
            return 0
        left = self.dfs(d, node.left)
        right = self.dfs(d, node.right)
        depth = max(left, right) + 1
        d[depth].append(node.val)
        return depth