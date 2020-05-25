def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    res = []
    while root:
        res.append(root.data)
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            break
    # print(res)
    for n in res:
        print(n, end=' ')
    return res