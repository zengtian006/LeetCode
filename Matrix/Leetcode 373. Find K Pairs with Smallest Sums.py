class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        h = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(h, (i+j, [i, j]))
        res = []
        while h and k>0:
            sums, [i,j] = heapq.heappop(h)
            res.append([i,j])
            k-=1
        return res