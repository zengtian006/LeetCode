class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i < len(nums):
            if i<len(nums)-1 and nums[i]+1 == nums[i+1]:
                start = i
                while i<len(nums)-1 and nums[i]+1 == nums[i+1]:
                    i+=1
                res.append(str(nums[start])+"->"+str(nums[i]))
            else:
                res.append(str(nums[i]))
            i+=1
        return res