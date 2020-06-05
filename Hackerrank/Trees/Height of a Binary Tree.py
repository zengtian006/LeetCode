def getHeight(root):
    if not root:
        return 0 
    left = getHeight(root.left)
    right = getHeight(root.right)
    return 1+max(left, right)

def height(root):
    height = getHeight(root)
    return height-1