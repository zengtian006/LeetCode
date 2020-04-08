class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost, rightmost = 0, 0
        left, right = 0, len(height)-1
        res = 0
        while left<right:
            leftmost = max(height[left],leftmost)
            rightmost = max(height[right],rightmost)
            if leftmost <= rightmost:
                res += leftmost - height[left]
                left+=1
            else:
                res += rightmost - height[right]
                right-=1
        return res