# Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val) 

        
# Iterative
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = []
        stack.append((root, sum))
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right and node.val == s:
                return True
            if node.left:
                stack.append((node.left, s-node.val))
            if node.right:
                stack.append((node.right, s-node.val))
        return False