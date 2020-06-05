def getRegion(arr, x, y):
    region = 0
    for i in range(3):
        for j in range(3):
            if i == 1 and (j ==0 or j ==2):
                continue
            region+=arr[x+i][y+j]
    return region


def hourglassSum(arr):
    if not arr:
        return -1
    m, n = len(arr), len(arr[0])
    if m<3 or n<3:
        return -1
    res = float('-inf')
    for i in range(m-2):
        for j in range(n-2):
            region = getRegion(arr, i, j)
            res = max(res, region)
    return res