class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        dic = collections.defaultdict(dict)
        return self.helper(nums, 0, S, dic)
        return (self.res)
    
    def helper(self, nums, idx, S, dic):
        if idx == len(nums):
            if S == 0:
                return 1
            else:
                return 0
        if S in dic[idx]:
            return dic[idx][S]
        x = self.helper(nums, idx+1, S-nums[idx], dic)
        y = self.helper(nums, idx+1, S+nums[idx], dic)
        dic[idx][S] = x+y
        return dic[idx][S]
        