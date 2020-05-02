# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        l,r,p = root.left, root.right, root
        res = []
        if root.right or root.left:
            res.append(root.val)
        
        #left b
        while l and (l.left or l.right):
            res.append(l.val)
            if l.left:
                l = l.left
            elif l.right:
                l = l.right
                
        #leaves:
        stack = [p]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        #right b
        rb = []
        while r and (r.left or r.right):
            rb.append(r.val)
            if r.right:
                r = r.right
            elif r.left:
                r = r.left
        if rb:
            res.extend(rb[::-1])
        return res