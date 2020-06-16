# Union Find


Union Find 主要可以检测图是否存在环，或者验证是否是树。 

Union Find 主要有两个函数，Union 和 Find,  Union的作用是检测两个联通的点是够再同一个集合，如果不再同一个集合，则将其中一个点Union到另一个点的集合中，如果在同一个集合，则说明有环; Find的作用是查找某个点属于哪个集合。


- 举例

    - 有6个点，有这几条边 edges = [(0, 2), (4, 1), (2, 3), (3, 5), (1, 3)]

    1. -初始值有5个集合： [0],[1],[2],[3],[4],[5]
    2. (0,2), 0跟2连接，所以 [0,2],[1],[3],[4],[5]
    3. (4,1), 4跟1连接，所以 [0,2],[3],[4,1],[5]
    4. (2,3), 2跟3连接，所以 [0,2,3],[4,1],[5]
    5. (3,5), 3跟5连接，所以 [0,2,3,5],[4,1]
    6. (1,3), 1跟3连接，所以 [0,2,3,5,4,1] 
        验证成功，为树，无环

    - 有6个点，有这几条边 edges = [(0, 5), (4, 0), (1, 2), (4, 5), (3, 2)]

    1. -初始值有5个集合： [0],[1],[2],[3],[4],[5]
    2. (0,5), 0跟5连接，所以 [0,5],[1],[2],[3],[4]
    3. (4,0), 4跟0连接，所以 [0,5,4],[1],[2],[3]
    4. (1,2), 1跟2连接，所以 [0,5,4],[1，2],[3]
    5. (4,5), 4跟5连接，所以 [0,5,4],[1，2],[3]
        4 跟 5 同属一个集合，所有有环，不是树


- 基本操作

```python

class UnionFind:
    def __init__(self, n):
        # 有n个结点，初始值每个节点属于只含有自己本身的集合
        self.parent = [i for i in range(n)]

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        return root # 找到A点的集合，返回该集合的root点

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return #有环
        self.parent[root_A] = root_B # 将A所在的集合跟B连通
        return
```

- 练习题
[Leetcode 261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/description/)
[Leetcode 323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)