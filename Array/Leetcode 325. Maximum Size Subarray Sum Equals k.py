class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        preSum = [0]*(len(nums)+1)
        preSum[0] = 0
        for i in range(1, len(nums)+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        

        dic = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i] not in dic:
                dic[preSum[i]] = i
            if preSum[i]-k in dic:
                res = max(res, i-dic[preSum[i]-k])
        return res


# 求数组某部分连续的合，考虑创建一个PreSum数组： 数组i 到 j的和 = presum[j+1] - presum[i]的合