# improved recursive
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.helper(nums, 0,[], res)
        return list(res)
    
    def helper(self, nums, idx, tempList, res):
        if len(tempList)>1:
            # if tempList not in res:
            res.add(tuple(tempList))

        for i in range(idx, len(nums)):
            if not tempList or nums[i] >= tempList[-1]:
                self.helper(nums, i+1, tempList+[nums[i]], res)


# recursive
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0,[], res)
        return res
    
    def helper(self, nums, idx, tempList, res):
        if len(tempList)>1:
            if tempList not in res:
                res.append(tempList)
        for i in range(idx, len(nums)):
            if not tempList or nums[i] >= tempList[-1]:
                self.helper(nums, i+1, tempList+[nums[i]], res)


# Iterative
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        visited = set()
        for i in range(len(nums)):
            stack.append(([nums[i]], i))
            while stack:
                lst,idx = stack.pop()
                if len(lst)>1:
                    if lst not in res:
                        res.append(lst)
                for j in range(idx+1,len(nums)):
                    if nums[j] >= lst[-1] and tuple(lst+[nums[j]]) not in visited:
                        stack.append((lst+[nums[j]], j))
                        visited.add(tuple(lst+[nums[j]]))
        return res