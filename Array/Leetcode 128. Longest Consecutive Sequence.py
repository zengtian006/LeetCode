class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num - 1 not in s:
                cur_num = num
                count = 1
                while cur_num + 1 in s:
                    cur_num += 1
                    count += 1
                res = max(res, count)
        return res

# 只往后面找连续数字，比如3 只找4，5，6 不找2，1