import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q,-num)
        res = 0
        for _ in range(k):
            res = heapq.heappop(q)
        return -res