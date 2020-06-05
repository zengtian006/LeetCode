#有没有可能删除一个字符，使所有字符出现的次数一样

# aabbcd -> NO
# aabbccddeefghi -> NO
# aabbc -> YES 删除c
# abcdd -> YES  删除d

import collections
# Complete the isValid function below.
def isValid(s):
    if not s:
        return "YES"
    dic = {}
    for c in s:
        dic[c] = dic.get(c,0)+1
    
    freq = collections.defaultdict(list)
    for k,v in dic.items():
        freq[v].append(k)
    print(freq)
    if len(freq.keys())>2:
        return "NO"
    if len(freq.keys()) == 1:
        return "YES"
    
    keys = list(freq.keys())
    if (abs(keys[0] - keys[1]) == 1 and (len(freq[keys[0]])==1 or len(freq[keys[1]]) == 1)) or (keys[0] == 1 and len(freq[keys[0]])==1) or (keys[1] == 1 and len(freq[keys[1]])==1):
        return "YES"
    return 'NO'