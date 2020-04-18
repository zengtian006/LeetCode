collections
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return 
        q = collections.deque()
        dic = collections.defaultdict(list)
        q. append((root, 0))
        while q:
            size = len(q)
            for _ in range(size):
                node, v = q.popleft()
                dic[v].append(node.val)
                if node.left:
                    q.append((node.left, v-1))
                if node.right:
                    q.append((node.right, v+1))
        res = []
        for k in sorted(dic.keys()):
            res.append(dic[k])
        return res