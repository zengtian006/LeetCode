# https://www.hackerrank.com/challenges/pairs/problem
def pairs(k, arr):
    dic = {}
    count = 0
    for i,a in enumerate(arr):
        if a-k in dic:
            count +=1
        if a+k in dic:
            count += 1
        dic[a] = i
    return count