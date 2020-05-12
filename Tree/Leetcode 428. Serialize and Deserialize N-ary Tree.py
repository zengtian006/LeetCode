"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            chs = len(node.children) if node.children else 0
            res.append(str(node.val)+' '+str(chs))
            for ch in node.children:
                q.append(ch)
        return ",".join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = data.split(',')
        r, c = data[0].split(' ')
        root = Node(int(r), [])
        q = collections.deque()
        q.append((root,int(c)))
        idx = 1
        while q:
            node, count = q.popleft()
            for _ in range(count):
                val, cnt = data[idx].split(' ')
                n = Node(int(val),[])
                node.children.append(n)
                q.append((n, int(cnt)))
                idx+=1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))