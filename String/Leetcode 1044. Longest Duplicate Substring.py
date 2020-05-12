class Solution:
    def longestDupSubstring(self, S: str) -> str:
        nums = [ord(S[i])-ord('a') for i in range(len(S))]
        left, right = 1, len(S)-1
        while left<=right:
            mid = left+(right-left)//2
            if self.helper(mid, nums)!=-1:
                left = mid + 1
            else:
                right = mid - 1
        start = self.helper(left-1, nums)
        return S[start: start+left-1] if start != -1 else ""
        
    def helper(self, pos, nums):
        h = 0
        for i in range(pos):
            h = (h*26 + nums[i])%(2**32)
        
        aL = 26**pos %(2**32)
        visited = set()
        visited.add(h)
        for start in range(1, len(nums)-pos+1):
            h = ((h*26 - nums[start-1]*aL)+nums[start+pos-1])%(2**32)
            if h in visited:
                return start
            visited.add(h)
        return -1


# https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode/