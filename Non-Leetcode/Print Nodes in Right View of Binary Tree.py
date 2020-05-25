def rightView(root):
    '''
    :param root: root of given tree.
    :return: print the right view of tree, dont print new line
    '''
    if not root:
        return
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size-1:
                res.append(node.data)
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    for c in res:
        print(c, end=' ')
    return res