class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]
        res = 0
        n = len(heights)
        for j in range(n):
            if j == n-1 or heights[j] > heights[j+1]:
                min_height = heights[j]
                for i in range(j,-1,-1):
                    min_height = min(heights[i], min_height)
                    wid = j-i+1
                    area = min_height*wid
                    res = max(res, area)
        return res


#我们只需在这些局部峰值出进行处理(height[i] > height[i+1])，为什么不用在非局部峰值处统计呢，这是因为非局部峰值处的情况，后面的局部峰值都可以包括，比如1和5，由于局部峰值6是高于1和5的，所有1和5能组成的矩形，到6这里都能组成，并且还可以加上6本身的一部分组成更大的矩形，那么就不用费力气去再统计一个1和5处能组成的矩形了