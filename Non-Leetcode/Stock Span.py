# https://www.geeksforgeeks.org/the-stock-span-problem/amp/

# input {100, 80, 60, 70, 60, 75, 85}
# output {1, 1, 1, 2, 1, 4, 6}

def calculateSpan(prices):
  res = [0]*len(prices)

  res[0] = 1
  stack = []
  stack.append(0)
  for i in range(1, len(prices)):
    while stack and prices[i] >= prices[stack[-1]]:
      stack.pop()
    res[i] = i-stack[-1]
    stack.append(i)

  print(res)

calculateSpan([100, 80, 60, 70, 60, 75, 85])