# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def superDigit(n, k):
    sums = 0
    for i in range(len(n)):
        sums += int(n[i])
    
    sums *= k
    while sums > 9:
        s = 0
        while sums > 0:
            s += sums % 10
            sums //= 10
        sums = s
    return sums