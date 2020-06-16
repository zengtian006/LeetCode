# Topological Sort


- 需要计算所有点的入度和出度，其核心是BFS 
- 步骤
1. 一般是有向图，构建Graph，将入度为0的点放入Queue中, 
2. 每次从Queue中拿出一个点，放入res，遍历这个点的出度(子结点)
    1. 子节点的入度减1
    2. 如果更新后的入度为0， 则放入Queue中
3. 最终res就是排序好的数组


- 代码
```python
# lst = [0,1], [1,2] ..... 意思是0指向1， 1 指向2， 等等

def topoSort(self, lst, n):
    parent = collections.default(int) # 入读
    child = collections.default(list) # 出度
    for x, y in lst:
        child[x].append(y)  # y 是 x 的子节点
        parent[y] = x 

    q = collections.deqeu()
    for i in range(n):
        if parent[i] == 0:
            q.append(i)
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for ch in child[node]:
            parent[ch] -= 1
            if parent[ch] == 0:
                q.append(ch)
    return res
```

- 练习

[Leetocde 207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

[Leetcode 210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

[Leetcode 269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)