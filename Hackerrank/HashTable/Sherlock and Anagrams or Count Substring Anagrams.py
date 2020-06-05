# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
def anagramPairs(s):
    # Write your code here
    dic = {}
    res = 0
    for k in range(1, len(s)):
        for i in range(len(s)-k+1):
            j = i+k
            strr = "".join(sorted(s[i:j]))
            dic[strr] = dic.get(strr,0)+1
    for v in dic.values():
        if v>1:
            res += (v*(v-1))//2
    return res