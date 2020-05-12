def topView(root):
    '''
    :param root: root of the binary tree
    :return: None, newline is provided by driver code
    '''
    # code here
    if not root:
        return ''
    dic = {}
    q = collections.deque()
    q.append((root,0))
    res = []
    while q:
        node, c = q.popleft()
        if c not in dic:
            dic[c] = node.data
        if node.left:
            q.append((node.left, c-1))
        if node.right:
            q.append((node.right, c+1))
    for k in sorted(dic.keys()):
        res.append(dic[k])
    return res

# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/