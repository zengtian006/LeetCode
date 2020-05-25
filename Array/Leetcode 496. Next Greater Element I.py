class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        dic = {}
        for i in range(1, len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                idx = stack.pop()
                dic[nums2[idx]] = nums2[i]
            stack.append(i)
        res = []
        for num in nums1:
            if num in dic:
                res.append(dic[num])
            else:
                res.append(-1)
        return res