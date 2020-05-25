# Find the range of shortest subarray which when removed will make the remaining elements in the array sorted?

# Ex:
# [1, 2, 3, 99, 4, 2, 3, 5]
# Ans: [3, 5] - { 99, 4, 2 } which when removed will make array { 1, 2, 3, 3, 5} which is sorted.

# ii) [1, 2, 3, 4 , 5]
# Ans: []

# iii) [5, 4, 3, 2 ,1]
# Ans: [0, 3]
# But, [1, 4] is also a valid answer.

# https://leetcode.com/discuss/interview-question/592517/Amazon-Interview-Question-SDE-II


class Solution:
    def SSR(self, nums) -> int:
        nums = [1, 2, 3, 99, 4, 2, 3, 5]
        nums = [1, 2, 3, 4 , 5]
        nums = [5, 4, 3, 2 ,1]
        left, right = 0, len(nums)-1
        res =[-1]*2
        min_len = len(nums)
        while right>0 and nums[right]>=nums[right-1]:
            right -= 1
        res[0] = 0
        res[1] = right -1
        while left < right and nums[left]<=nums[left+1]:
            while right<len(nums) and nums[left]>nums[right]:
                right += 1
            if right <len(nums) and nums[left]<=nums[right]:
                if right -left-1 < min_len:
                    min_len = right-left -1
                    res[0] = left+1
                    res[1] = right-1
            left += 1
        
        print(res)
        return res
        

