class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #对于每一个高度height，计算前一个小于该高度的位置，left；和后一个小于该高度的位置，left。面积就等于height*(right-left-1)
        stack = [-1]
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                height = heights[stack.pop()]
                right = i
                left = stack[-1]
                res = max(res, height*(right-left-1))
            stack.append(i)
        return res


# Optimized Bruce force
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]
                res = 0
                for i in range(len(heights)):
                    if i == len(heights)-1 or heights[i]>heights[i+1]:
                        minHeight = heights[i]
                        for j in range(i,-1,-1):
                            minHeight = min(minHeight, heights[j])
                            res = max(res, minHeight*(i-j+1))
                return res
    
#看题目中的例子，局部峰值为 2，6，3，我们只需在这些局部峰值出进行处理，为啥不用在非局部峰值处统计呢，这是因为非局部峰值处的情况，后面的局部峰值都可以包括，比如1和5，由于局部峰值6是高于1和5的，所有1和5能组成的矩形，到6这里都能组成，并且还可以加上6本身的一部分组成更大的矩形，那么就不用费力气去再统计一个1和5处能组成的矩形了