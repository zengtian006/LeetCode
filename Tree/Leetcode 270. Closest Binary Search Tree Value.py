class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        mn = float('inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if abs(node.val-target) < mn:
                mn = abs(node.val-target) 
                res = node.val
            root = node.right
        return res
