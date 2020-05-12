class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right =node.right, node.left
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root