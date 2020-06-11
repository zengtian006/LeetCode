# Tree Traversal

## 前序遍历 ([Leetcode 144](https://leetcode.com/problems/binary-tree-preorder-traversal/))

1. 递归 

```python
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return res
```

2. 迭代(非递归)

```python
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```

## 中序遍历 ([Leetcode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/))

1. 递归

```python
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        return res
```

2. 迭代

```python
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            if node.right:
                root = node.right
        return res
```       

## 后序遍历 ([Leetcode 145](https://leetcode.com/problems/binary-tree-postorder-traversal/))

1. 递归

```python
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        helper(root)
        return res
```

2. 迭代

第一种方法，后续遍历的顺序式，left->right->root  可以先进行反向的前序遍历 root->right->left， 再将结果翻转

```python
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
```

第二种方法

```python
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        pre, cur = None, root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                top = stack[-1]
                if top.right and top.right!=pre:
                    cur = top.right
                else:
                    res.append(top.val)
                    pre = top
                    stack.pop()
        return res
```

## 层序遍历 (BFS)

```python
    def levelTraversal(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return res
```

## DFS
```python
    def DFSTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res
```

[Tree Traversal Leetcode 练习题](https://github.com/zengtian006/LeetCode/tree/master/Tree)

[Top/Bottom/Left/Right view of Binary Tree](https://github.com/zengtian006/LeetCode/tree/master/Non-Leetcode)
