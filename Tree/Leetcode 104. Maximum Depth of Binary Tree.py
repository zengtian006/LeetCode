class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        stack = []
        stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                res = max(res, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return res

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1
        