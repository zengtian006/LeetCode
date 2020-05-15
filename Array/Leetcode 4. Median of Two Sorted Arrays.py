# 时间复杂度 O((m+n)*log(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1),len(nums2)
        
        l = l1+l2
        n = l//2
        heap = []
        i = j = 0
        if nums1:
            heapq.heappush(heap, nums1[i])
        if nums2:
            heapq.heappush(heap, nums2[j])
        while n>0:
            x1 = heapq.heappop(heap)
            if nums1 and x1 == nums1[i] and i<l1-1:
                i+=1
                heapq.heappush(heap, nums1[i])
            elif nums2 and x1 == nums2[j] and j<l2-1:
                j+=1
                heapq.heappush(heap, nums2[j])
            n-=1
        x2 = heap[0]
        if l%2 == 0:
            return (x1+x2)/2
        else:
            return x2