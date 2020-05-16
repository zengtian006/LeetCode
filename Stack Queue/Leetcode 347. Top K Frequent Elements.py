class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        bucket = [0]*(len(nums)+1)
        for num in nums:
            dic[num] = dic.get(num, 0) +1
            
        for key, count in dic.items():
            if bucket[count] == 0:
                bucket[count] = []
            bucket[count].append(key)
            
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i] != 0:
                res.extend(bucket[i])
                k -= len(bucket[i])
                if k<=0:
                    return res