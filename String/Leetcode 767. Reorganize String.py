class Solution:
    def reorganizeString(self, S: str) -> str:
        dic = {}
        for s in S:
            dic[s] = dic.get(s,0)+1
        
        h = []
        for k,v in dic.items():
            if v>(len(S)+1)//2:
                return ''
            heapq.heappush(h, (-v, k))
        res = ""
        while len(h)>1:
            count, char = heapq.heappop(h)
            if res and char == res[-1]:
                c, ch  = count, char
                count, char = heapq.heappop(h)
                heapq.heappush(h, (c, ch))
            res += char
            if count != -1:
                count += 1
                heapq.heappush(h, (count, char))
        while h:
            count, char = heapq.heappop(h)
            res += char
        return res