class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre and node.val <= pre.val:
                return False
            root,pre = node.right,node
        return True