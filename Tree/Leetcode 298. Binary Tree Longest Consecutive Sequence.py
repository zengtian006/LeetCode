# Recursive
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 1
        self.helper(root, 1)
        return self.res
    
    def helper(self, node, v):
        self.res = max(self.res, v)
        if node.left:
            if node.left.val == node.val+1:
                self.helper(node.left,v+1)
            else:
                self.helper(node.left, 1)
        if node.right:
            if node.right.val == node.val+1:
                self.helper(node.right,v+1)
            else:
                self.helper(node.right, 1)


# Iterative
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        res = 1
        stack = []
        stack.append((root, 1))
        while stack:
            node, l = stack.pop()
            res = max(res, l)
            if node.left:
                if node.left.val == node.val+1:
                    stack.append((node.left, l+1))
                else:
                    stack.append((node.left, 1))
            if node.right:
                if node.right.val == node.val+1:
                    stack.append((node.right, l+1))
                else:
                    stack.append((node.right, 1))
        return res