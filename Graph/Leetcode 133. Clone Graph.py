class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        dic = {}
        q = collections.deque()
        q.append(node)
        dic[node] = Node(node.val, [])
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                dic[n].neighbors.append(dic[neighbor])
        return dic[node]