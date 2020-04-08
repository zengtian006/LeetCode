class Solution:
    def jump(self, nums: List[int]) -> int:
        curMax = preMax = 0
        res = 0
        for i in range(len(nums)-1):
            curMax = max(curMax, nums[i]+i)
            if i == preMax:
                res += 1
                preMax = curMax
        return res

#preMax 指的是上一步走的最大距离，一旦走到preMax，step+1，并且更新preMax为curMax(curMax是preMax范围内的最大距离)，因为题目假设一定可以到达最终，所以也可不需要在preMax范围内求curMax，只需一直计算curMax即可