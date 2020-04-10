class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        res = len(nums)+1
        sums = 0
        for j in range(len(nums)):
            sums += nums[j]
            while sums >=s:
                res = min(res, j-i+1)
                sums -= nums[i]
                i+=1
        return res if res<len(nums)+1 else 0