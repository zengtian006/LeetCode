class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        l = self.height(root.left)
        r = self.height(root.right)
        return abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, node):
        if not node: return 0
        return 1+max(self.height(node.left), self.height(node.right))