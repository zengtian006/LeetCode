class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        visited = set()
        res = []
        parent = {}
        self.findParent(root, parent)
        self.helper(target, K, visited, parent, res)
        return res
        
    def findParent(self, node, parent):
        if not node:
            return 
        if node.left:
            parent[node.left] = node
        if node.right:
            parent[node.right] = node
        self.findParent(node.left, parent)
        self.findParent(node.right, parent)
        
    def helper(self, node, k, visited, parent, res):
        if node in visited:
            return
        if k == 0:
            res.append(node.val)
            return
        visited.add(node)
        if node.left:
            self.helper(node.left, k-1, visited, parent, res)
        if node.right:
            self.helper(node.right, k-1, visited, parent, res)    
        if node in parent:
            self.helper(parent[node], k-1, visited, parent, res)