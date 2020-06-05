def makeAnagram(a, b):
    dic1 = {}
    dic2 = {}
    chars = set()
    for c in a:
        dic1[c] = dic1.get(c, 0)+1
        chars.add(c)
    for c in b:
        dic2[c] = dic2.get(c, 0)+1
        chars.add(c)

    res = 0 
    for c in chars:
        if (c in dic1 and c not in dic2) or (c in dic2 and c not in dic1):
            res += dic1[c] if c in dic1 else dic2[c]
        elif c in dic1 and c in dic2:
            res += abs(dic1[c]-dic2[c])
    return res