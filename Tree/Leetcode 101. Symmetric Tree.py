class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isSame(root.left, root.right)
    
    def isSame(self, p, q):
        if not p and not q:return True
        if not p or not q: return False
        if p.val != q.val:
            return False
        return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)