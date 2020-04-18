class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            nxt = None
            for _ in range(size):
                node = q.popleft()
                node.next = nxt
                nxt = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root