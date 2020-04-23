import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        heap = []
        for key,count in dic.items():
            heapq.heappush(heap, (-count,key))
        
        res = []
        for i in range(k):
            count, key = heapq.heappop(heap)
            res.append(key)
        return res