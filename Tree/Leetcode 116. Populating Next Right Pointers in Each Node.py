# Recursive
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

# BFS
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