class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low,hight, n = 0, len(citations)-1, len(citations)
        while low<=hight:
            middle = low+(hight-low)//2
            if (n - middle) == citations[middle]:
                return citations[middle]
            if (n - middle) < citations[middle]:
                hight = middle -1
            if (n - middle) > citations[middle]:
                low = middle +1 
        return n-low