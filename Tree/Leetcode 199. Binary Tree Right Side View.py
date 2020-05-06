class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res