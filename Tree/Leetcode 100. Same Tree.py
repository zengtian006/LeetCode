class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:return True
        if not p or not q: return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        q = collections.deque([(p, q)])
        while q:
            n1,n2 = q.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            q.append((n1.left, n2.left))
            q.append((n1.right, n2.right))
        return True