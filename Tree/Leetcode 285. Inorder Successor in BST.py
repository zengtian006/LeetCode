class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        found = False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if found:
                return node
            if node.val == p.val:
                found = True
            root = node.right