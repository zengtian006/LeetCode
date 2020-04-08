class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstSmall = secondSmall = float('inf')
        for num in nums:
            if num <= firstSmall:
                firstSmall = num
            elif num <= secondSmall:
                secondSmall = num
            else:
                return True
        return False

# 找到前两个最小数字，如果后面的数字比这两个数字大，则True