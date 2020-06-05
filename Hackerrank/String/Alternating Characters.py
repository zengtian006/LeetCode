def alternatingCharacters(s):
    i = 0
    j = 1
    count = 0
    while j<len(s):
        if s[j] == s[i]:
            while j<len(s) and s[j] == s[i]:
                j+=1
            count += j-i-1
        i = j
        j += 1
    return count