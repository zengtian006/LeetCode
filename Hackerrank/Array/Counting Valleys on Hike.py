def countingValleys(n, s):
    height = 0
    pre_height = 0
    count = 0
    for c in s:
        if c == 'U':
            height += 1
        else:
            height -= 1
        if height == 0 and pre_height < 0:
            count += 1
        pre_height = height
    return count