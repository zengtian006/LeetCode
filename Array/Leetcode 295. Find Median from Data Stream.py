import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        self.l = 0


    def addNum(self, num: int) -> None:
        if not self.minHeap or self.minHeap[0]<=num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
            
        #balancing max and min heap
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        elif len(self.maxHeap) > len(self.minHeap):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        self.l += 1

        
    def findMedian(self) -> float:
        val1 = self.minHeap[0]
        if self.l % 2 == 1:
            return val1
        else:
            val2 = -self.maxHeap[0]
            return (val1+val2)/2

# 用一个大堆 一个小堆，例如 1，2，3，4，5  大堆为[1,2] 小堆为[3,4,5]
# 取中位数就是： 若总长为奇数， 取最小堆的最小值；若总长为偶数 数小堆最小值 和大堆的最大值 除2， 