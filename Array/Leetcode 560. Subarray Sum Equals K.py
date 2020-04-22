class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            preSum[i+1] = preSum[i]+nums[i]
        dic = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i] - k in dic:
                res += dic[preSum[i] - k ]
            dic[preSum[i]] = dic.get(preSum[i],0)+1
        return res