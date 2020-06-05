def numberPairs(n, ar):

    # Write your code here
    dic = {}
    count = 0
    for a in ar:
        if a in dic:
            count += 1
            del dic[a]
        else:
            dic[a] = 1
    return count