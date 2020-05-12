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


# Quick sort
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = self.getPivot(nums)
        
        if p+1 == k: return nums[p]
        elif p+1 > k: return self.findKthLargest(nums[:p], k)
        else: return self.findKthLargest(nums[p+1:],k-1-p)
        
    def getPivot(self, nums):
        lo,hi = 0, len(nums)-1
        if lo>=hi: return lo
        self.swap(nums, random.randrange(lo,hi,1), hi)
        i = lo
        for j in range(lo, hi):
            if nums[j]>nums[hi]:
                self.swap(nums, i , j)
                i+=1
        self.swap(nums,i,hi)
        return i
        
    def swap(self, nums, i ,j):
        nums[i], nums[j] = nums[j], nums[i]
        return nums