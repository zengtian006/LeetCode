# https://www.hackerrank.com/challenges/minimum-time-required/problem

def calItems(machines, goal, days):
    items = 0
    for m in machines:
        items += days//m
        if items >=goal:
            break
    return items

def minTime(machines, goal):
    left, right = 0, max(machines)*goal
    while left<=right:
        mid = left + (right-left)//2
        items = calItems(machines,goal, mid)
        if items>=goal:
            right = mid - 1
        else:
            left = mid + 1
    return right+1





# another solution
def minTime(machines, goal):
    h = []
    for i in range(len(machines)):
        heapq.heappush(h, (machines[i], i))
    days = 0
    while goal>0:
        goal -= 1
        d, i = heapq.heappop(h)
        days += d-days
        heapq.heappush(h, (d+machines[i], i))
    return days