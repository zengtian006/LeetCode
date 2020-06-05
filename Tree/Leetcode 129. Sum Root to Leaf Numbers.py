class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = []
        stack.append((root,str(root.val)))
        while stack:
            node, strr = stack.pop()
            if not node.left and not node.right:
                res+=int(strr)
            if node.left:
                stack.append((node.left, strr+str(node.left.val)))
            if node.right:
                stack.append((node.right, strr+str(node.right.val)))
        return res