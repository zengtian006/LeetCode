def jumpingOnClouds(c):
    pre_max = cur_max = 0
    steps = 0
    for i in range(len(c)):
        if pre_max >= len(c)-1:
            return steps
        if c[i] == 1:
            continue
        local_max = 0
        if c[i] == 0:
            if i+1 < len(c) and c[i+1]!=1:
                local_max = i+1
            if i+2 < len(c) and c[i+2]!=1:
                local_max = i+2
        cur_max = max(cur_max, local_max)
        if i == pre_max:
            pre_max = cur_max
            steps += 1