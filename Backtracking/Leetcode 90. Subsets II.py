class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.bt(nums, 0, [], res)
        return res

    def bt(self, nums, idx, tempList, res):
        res.append(tempList)
        for i in range(idx,len(nums)):
            if i> idx and nums[i] == nums[i-1]:
                continue
            self.bt(nums, i+1, tempList+[nums[i]], res)