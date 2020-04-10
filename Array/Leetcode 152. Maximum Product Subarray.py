class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Because there is negaive digits, so we should store the minimum value for now -> cur_min
        res = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_max, cur_min = max(nums[i],nums[i]*cur_max, cur_min*nums[i]), min(nums[i],nums[i]*cur_max, cur_min*nums[i])
            res = max(res, cur_max)
        return res