class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return abs(left-right)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, node):
        if not node:
            return 0
        left =self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1