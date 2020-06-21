class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            node = stack.pop()
            k-=1
            if k == 0:
                return node.val
            root = node.left