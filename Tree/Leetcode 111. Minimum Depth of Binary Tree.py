import collections
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            size = len(q)
            for _ in range(size):
                node, depth = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))