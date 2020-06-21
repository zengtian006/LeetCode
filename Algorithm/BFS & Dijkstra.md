# BFS & Dijkstra

## BFS (Breadth-first search)

- BFS用Queue来实现，将根结点或者起始结点方式Queue中，然后开始遍历，每次将遍历到的节点放到Queue的结尾，不断popleft 不断append，直到Queue为空
- BFS 一般用来解决，层序遍历，或者最短距离

```python

    def BFS(self, root):
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)

    #如果要分层遍历，一般用来计算最短距离
    def BFS2(self, root)
        level = 0
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
            level+=1   
```

- 练习题

[Leetcode 200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

[Leetcode 127. Word Ladder](https://leetcode.com/problems/word-ladder/description/)

[Leetcode 994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

[Leetcode 815. Bus Routes](https://leetcode.com/problems/bus-routes/)


## Dijkstra

- 用Heap实现，每次从Heap中取路径最短的节点
- 维护另一个最短路径数组dist，并不断更新该数据，如果取出的路径加上nxt节点的路径大于dist[nxt]，则跳过
- 一般用来计算带权值的树或者图

```python
    def Dijkstra(self, graph, start, n):
        # assume 我们有个权值graph， graph[a][b] = 3 代表a点到b点的权值或距离是3
        dist = [float('inf')]*n
        dist[start] = 0
        h = []
        h.append((0, start))
        while heap:
            cost, node = heapq.heappop(h)
            for nxt in graph[h]:
                new_cost = cost + graph[h][nxt]
                if new_cost < dist[nxt]:
                    heapq.heappush(h, (new_cost, nxt))
                    dist[nxt] = new_cost

```

- 练习题

[Leetocde 787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

[Leetcode 743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
