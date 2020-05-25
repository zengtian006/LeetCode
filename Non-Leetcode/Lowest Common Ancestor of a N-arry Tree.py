class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Codec:
    def LCA(self, root: 'Node', p, q) -> str:
        q = 5
        p = 4
        if root.val == q or root.val == p:
            return root.val
        stack = []
        stack.append(root)
        parent = {}
        while stack and not (q in parent and p in parent):
            node = stack.pop()
            for ch in node.children:
                parent[ch.val] = node.val
                stack.append(ch)
        res = set()
        cur = q
        while cur in parent:
            res.add(cur)
            cur = parent[cur]
        res.add(root.val)
        cur = p
        while cur not in res:
            cur = parent[cur]
        return cur
        
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/ for Practice