# https://www.hackerrank.com/challenges/angry-children/problem

def maxMin(k, arr):
    arr.sort()
    res = float('inf')
    for i in range(len(arr)-k+1):
        j = i+k-1
        res = min(res, arr[j]-arr[i])
    return res