# Recursive
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.helper(root, sum, [], res)
        return res
    def helper(self,node, sum, path, res):
        if not node:
            return
        if not node.left and not node.right and node.val == sum:
            res.append(path+[node.val])
        self.helper(node.left, sum-node.val, path+[node.val], res)
        self.helper(node.right, sum-node.val, path+[node.val], res)


# Iterative
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = []
        res = []
        stack.append((root, [], sum))
        while stack:
            node, path, s = stack.pop()
            if not node.left and not node.right and node.val == s:
                res.append(path+[node.val]) 
            if node.left:
                stack.append((node.left, path+[node.val], s-node.val))
            if node.right:
                stack.append((node.right, path+[node.val], s-node.val))
        return res