# DFS

- DFS 一般有两种方法，一种是Recursive，另一种是Iterative(用stack 实现)
- 为了避免重复计算，会用hashmap或适用的数据结构维护一个visited变量
- 速度会比BFS要快，内存消耗小，因为每次只需要维护一个节点

1. Recursive

```python
    def DFS(self, matrix):
        m, n = len(matrix), len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "whatever conditions"  #满足什么条件：
                    self.helper(matrix, i, j, visited)
    def helper(self, matrix, x, y, visited):
        visited.add((x,y))
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(matrix), len(matrix[0])
        for dx, dy in dirs:
            nx = dx + x
            ny = dy + y
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and matrix[nx][ny] == 'whatever conditions':
                self.helper(matrix, nx, ny, visited)

    ## helper 也可以写成这样
    def helper(self, matrix, x, y, visited):
        m, n = len(matrix), len(matrix[0])
        if 0<=x<m and 0<=y<n and (x,y) not in visited and matrix[x][y] == 'whatever conditions':
            visited.add((x,y))
            self.helper(matrix, x+1, y, visited)
            self.helper(matrix, x-1, y, visited)
            self.helper(matrix, x, y+1, visited)
            self.helper(matrix, x, y-1, visited)
```

2, Iterative (Stack)

```python
    def DFS(self, martix):
        m, n = len(matrix), len(matrix[0])
        visited = set()
        stack = []
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "whatever conditions"  #满足什么条件：
                    stack.append((i,j)) # start point
                    visited.add((i,j))
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in dirs:
                            nx = dx + x
                            ny = dy + y
                            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and matrix[nx][ny] == 'whatever conditions':
                                stack.append((nx,ny))
                                visited.add((nx,ny))

```

- 练习题

[Leetcode 200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

[Leetcode 490. The Maze](https://leetcode.com/problems/the-maze/)

[Leetcode 329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)