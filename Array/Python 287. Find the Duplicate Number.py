class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            count = 0
            for num in nums:
                if num<=mid:
                    count+=1
            if count>mid:
                right = mid 
            else:
                left = mid + 1
        return right


# 从1.。n枚举， 如果mid是3， 再遍历nums，如果小于等于3的数大于3个，则重复数子一定在3以前(包括3)，反之则在3之后(不包括3)