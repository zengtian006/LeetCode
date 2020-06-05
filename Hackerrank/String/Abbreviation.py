# https://www.hackerrank.com/challenges/abbr/problem

# You can perform the following operations on the string, :

# Capitalize zero or more of 's lowercase letters.
# Delete all of the remaining lowercase letters in .
# Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

# For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.

# Function Description
# Complete the function  in the editor below. It must return either  or .
# abbreviation has the following parameter(s):

# a: the string to modify
# b: the string to match

def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = 1
    for i in range(1,m+1):
        if a[i-1].islower():
            dp[i][0] = dp[i-1][0]
            
    for i in range(1, m+1):
        for j in range(1,n+1):
            if a[i-1].upper() == b[j-1]:
                if a[i-1].islower():
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1]
            elif a[i-1].upper() != b[j-1]:
                if a[i-1].islower():
                    dp[i][j] = dp[i-1][j]
                
    return "YES" if dp[-1][-1] else "NO"