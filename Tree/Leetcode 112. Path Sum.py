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


# Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum)
        
    def helper(self, node, sum):
        if not node :
            return False
        if not node.left and not node.right:
            if node.val == sum:
                return True

        return self.helper(node.left, sum-node.val) or self.helper(node.right, sum-node.val)