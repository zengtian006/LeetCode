# Recursive
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return None
        res = []
        self.path(root, str(root.val), res)
        return res
    
    def path(self, root, s, res):
        if not root.left and not root.right:
            res.append(s)
            return
        if root.left:
            self.path(root.left, s+'->'+str(root.left.val), res)
        if root.right:
            self.path(root.right, s+'->'+str(root.right.val) , res)

# Iterative
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return
        res = []
        stack = []
        stack.append((root, str(root.val)))
        while stack:
            node, s = stack.pop()
            if node.left:
                stack.append((node.left, s+'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, s+'->'+str(node.right.val)))
            if not node.left and not node.right:
                res.append(s)
        return res
    
