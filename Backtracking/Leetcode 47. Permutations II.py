class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.bt(nums, [], set(), res)
        return res
    
    def bt(self, nums, tempList, used, res):
        if len(nums) == len(tempList):
            res.append(tempList)
            return
        for i in range(len(nums)):
            if i in used:
                continue
            if i > 0 and nums[i] == nums[i-1] and i-1 in used:
                continue
            used.add(i)
            self.bt(nums, tempList+[nums[i]], used, res)
            used.remove(i)