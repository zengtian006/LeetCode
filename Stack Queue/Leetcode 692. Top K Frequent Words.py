# bucket sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        bucket = [0]*len(words)
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        p = []
        for key,val in dic.items():
            if bucket[val] == 0:
                bucket[val] = []
            bucket[val].append(key)
           
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]!=0:
                if len(bucket[i])>k:
                    while k>0:
                        bucket[i].sort(reverse=True)
                        res.append(bucket[i].pop())
                        k-=1
                    return res
                res.extend(sorted(bucket[i]))
                k-=len(bucket[i])
                if k<=0:
                    return res

# heap
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        p = []
        for key,val in dic.items():
            heapq.heappush(p, (-val,key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(p)[1])
        return res