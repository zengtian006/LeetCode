import collections
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        s = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                s.append('null')
        res = ",".join(s)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        s = data.split(",")
        root = TreeNode(s[0])
        q = collections.deque()
        q.append(root)
        idx = 1
        while q:
            node = q.popleft()
            if node:
                node.left = TreeNode(s[idx]) if s[idx]!='null' else None
                q.append(node.left)
                idx+=1
                node.right = TreeNode(s[idx]) if s[idx]!='null' else None
                q.append(node.right)
                idx+=1
        return root