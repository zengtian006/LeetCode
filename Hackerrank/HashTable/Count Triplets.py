# https://www.hackerrank.com/challenges/count-triplets-1/problem

def countTriplets(arr, r):
    v2 = {}
    v3 = {}
    count = 0
    for a in arr:
        count += v3.get(a,0)
        if a in v2:
            v3[a*r] = v3.get(a*r,0)+v2[a]
        v2[a*r] = v2.get(a*r, 0) +1
    return count