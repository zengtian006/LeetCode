class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for s, d in sorted(tickets, reverse=True):
            dic[s].append(d)
        res = []
        stack = ['JFK']
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]