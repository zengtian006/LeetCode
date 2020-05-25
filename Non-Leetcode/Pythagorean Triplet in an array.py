# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.

def isTriplet(ar):  
  n = len(ar)
  for i in range(n): 
      ar[i] = ar[i] * ar[i] 
  ar.sort() 

  for i in range(n-1, 1, -1): 
      j = 0
      k = i - 1
      while (j < k): 
          if (ar[j] + ar[k] == ar[i]): 
              return True
          else: 
              if (ar[j] + ar[k] < ar[i]): 
                  j = j + 1
              else: 
                  k = k - 1
  return False
isTriplet([3, 1, 4, 6, 2])