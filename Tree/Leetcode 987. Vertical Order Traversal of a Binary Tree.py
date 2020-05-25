class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque()
        dic = collections.defaultdict(list)
        q.append((root,0))
        while q:
            size = len(q)
            temp = collections.defaultdict(list)
            for _ in range(size):
                node, idx = q.popleft()
                temp[idx].append(node.val)
                if node.left:
                    q.append((node.left, idx-1))
                if node.right:
                    q.append((node.right, idx+1))
            for key in temp:
                dic[key].extend(sorted(temp[key]))
            
        res = []
        for k in sorted(dic.keys()):
            res.append(dic[k])
        return res