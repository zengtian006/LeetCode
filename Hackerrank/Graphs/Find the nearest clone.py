# https://www.hackerrank.com/challenges/find-the-nearest-clone/forum

import collections
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    graph = collections.defaultdict(list)
    for x in range(len(graph_from)):
        graph[graph_from[x]].append(graph_to[x])
        graph[graph_to[x]].append(graph_from[x])
    for idx in ids:
        if idx == val:
            break
    q = collections.deque()
    q.append((idx,-1))
    step = 0
    while q:
        size = len(q)
        for _ in range(size):
            node, par = q.popleft()
            for nxt in graph[node]:
                if nxt != par:
                    if ids[nxt-1] == val:
                        return step+1
                    q.append((nxt,node))
        step += 1
    return -1