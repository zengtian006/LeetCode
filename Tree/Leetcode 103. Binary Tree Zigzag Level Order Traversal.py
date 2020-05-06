class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        reverse = False
        while q:
            temp = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if reverse:
                res.append(temp[::-1])
            else:
                res.append(temp)
            reverse = not reverse
        return res
