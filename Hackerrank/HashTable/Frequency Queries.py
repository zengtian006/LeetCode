# https://www.hackerrank.com/challenges/frequency-queries/problem
# You are given  queries. Each query is of the form two integers described below:
# -  : Insert x in your data structure.
# -  : Delete one occurence of y from your data structure, if present.
# -  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

# The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: .
import collections
def freqQuery(queries):
    dic = collections.defaultdict(int)
    freq = collections.defaultdict(list)
    res = []
    for q in queries:
        if q[0] == 1:
            f = dic[q[1]]
            if freq[f]:
                freq[f].remove(q[1])
            dic[q[1]] += 1
            freq[f+1].append(q[1])
        elif q[0] == 2:
            if dic[q[1]] > 0:
                f = dic[q[1]]
                dic[q[1]] -= 1
                freq[f].remove(q[1])
                if f - 1 >0:
                    freq[f-1].append(q[1])
        elif q[0] == 3:
            if q[1] in freq and freq[q[1]]:
                res.append('1')
            else:
                res.append('0')
    return res