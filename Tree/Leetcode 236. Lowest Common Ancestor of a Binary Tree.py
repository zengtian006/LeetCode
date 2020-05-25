# Iterative
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        if root == p or root == q:
            return root
        queue = collections.deque([root])
        parent = {}
        while not (p in parent and q in parent):
            u = queue.popleft()
            if u.left:
                parent[u.left] = u
                queue.append(u.left)
            if u.right:
                parent[u.right] = u
                queue.append(u.right)
        cur = q
        res = set([root])
        while cur in parent:
            res.add(cur)
            cur = parent[cur]
        cur = p
        while cur not in res:
            cur = parent[cur]
        return cur

# Recursive
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == q.val or root.val == p.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right