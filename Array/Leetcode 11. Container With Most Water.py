class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1
        while left<right:
            res = max(res, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return res
# 求面积 就要考虑左右边界，Two pointer
# 如果左边小于右边，left向左移，因为如果right向右移的化，肯定面积会更小