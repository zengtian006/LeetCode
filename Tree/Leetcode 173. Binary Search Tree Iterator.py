class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inOrder(root)
    
    def inOrder(self, node):
        s = []
        while s or node:
            while node:
                s.append(node)
                node = node.right
            node = s.pop()
            self.stack.append(node.val)
            node = node.left
        
        # if not node:
        #     return
        # self.inOrder(node.left)
        # self.stack.append(node.val)
        # self.inOrder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0