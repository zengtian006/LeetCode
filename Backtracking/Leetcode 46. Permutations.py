class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.bt(nums, [], res)
        return res
    
    def bt(self, nums, tempList, res):
        if len(tempList) == len(nums):
            res.append(tempList)
            return
        for i in range(len(nums)):
            if nums[i] in tempList:
                continue
            self.bt(nums, tempList+[nums[i]], res)