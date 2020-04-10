class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        left = lower
        for i in range(len(nums)):
            if nums[i]>left:
                if nums[i] == left+1:
                    res.append(str(left))
                else:
                    res.append(str(left)+"->"+str(nums[i]-1))
            left = nums[i]+1
        if upper == left:
            res.append(str(upper))
        elif upper > left:
            res.append(str(left)+"->"+str(upper))
        return res