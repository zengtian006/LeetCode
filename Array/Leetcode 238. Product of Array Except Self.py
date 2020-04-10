class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd, bwd = [0]*n, [0]*n
        res = [0]*n
        fwd[0] = 1
        for i in range(1,n):
            fwd[i] = fwd[i-1] * nums[i-1]
        bwd[-1] = 1
        for i in range(n-2,-1,-1):
            bwd[i] = bwd[i+1] * nums[i+1]
        for i in range(n):
            res[i] = fwd[i]*bwd[i]
        return res