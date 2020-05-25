class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dummy = Node(-1)
        pre = dummy
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            pre.right = cur
            cur.left = pre
            pre = cur
            root = cur.right
        head = dummy.right
        head.left = pre
        pre.right = head
        return head