class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        p1 = self.helper(root.left, root.val, -1)+self.helper(root.right, root.val, 1) + 1
        p2 = self.helper(root.left, root.val, 1)+self.helper(root.right, root.val, -1) + 1
        
        throughRoot = max(p1,p2)
        notThroughToor = max(self.longestConsecutive(root.left), self.longestConsecutive(root.right))
        return max(throughRoot, notThroughToor)

    def helper(self, root, pre, diff):
        if not root:
            return 0
        if root.val == pre+diff:
            left = self.helper(root.left, root.val, diff)
            right = self.helper(root.right, root.val, diff)
            return max(left,right)+1
        else:
            return 0