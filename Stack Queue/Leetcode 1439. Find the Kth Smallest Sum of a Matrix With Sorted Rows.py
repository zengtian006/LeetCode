import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        res = self.helper(mat, k)
        return res[k-1]
    
    def helper(self, mat, k):
        if len(mat) == 1:
            return mat[0]
        mid = len(mat)//2
        l1 = self.helper(mat[:mid], k)
        l2 = self.helper(mat[mid:], k)
        return self.merge(l1, l2, k)
    
    def merge(self, l1, l2, k):
        res = []
        if not l1 or not l2 or not k:
            return res
        heap = []
        for i in l1:
            for j in l2:
                heapq.heappush(heap, i+j)
        while heap and k>0:
            res += [heapq.heappop(heap)]
            k-=1
        return res

# Divide and Conquer