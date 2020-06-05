def repeatedString(s, n):
    count = 0
    for c in s:
        if c == 'a':
            count += 1
    k = n//len(s)
    res = count*k
    rest = n%len(s)

    for i in range(rest):
        if s[i] == 'a':
            res += 1
    return res