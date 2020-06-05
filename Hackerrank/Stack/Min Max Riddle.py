# https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/
def riddle(arr):
    # complete this function
    res = []
    for k in range(1, len(arr)+1):
        local_max = float('-inf')
        for i in range(len(arr)-k+1):
            j = i+k
            local_max = max(local_max, min(arr[i:j]))
        res.append(local_max)
    return res