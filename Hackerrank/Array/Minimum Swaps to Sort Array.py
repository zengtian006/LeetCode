# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# Explaination :https://www.youtube.com/watch?v=J9ikRMK8Yhs

def minimumSwaps(arr):
    dic = {}
    for i in range(len(arr)):
        dic[i+1] =arr[i]
    visited = [0]*(len(arr)+1)
    visited[0] = 1
    res = 0
    for i in range(1,len(arr)+1):
        if visited[i] or dic[i] == i:
            continue
        j = i
        circle = 0
        while not visited[j]:
            visited[j] = 1
            j = dic[j]
            circle+=1
        res += circle -1
    return res