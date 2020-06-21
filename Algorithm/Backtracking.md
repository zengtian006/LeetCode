# BackTracking

- 基本上回溯分为两种， 一种为Subsets， 一种为Permutations
- Subsets 的特点是，每次从给定数组的下一个位置开始尝试每一个字符,要维护一个当前位置的的变量idx，尝试完之后再删除
- Permutations的特点是，每次都从给定数组的起始位置尝试，如果该字符尝试过了(可能要维护一个visited set)，就continue
- 一般来说，Subset 类型的时间复杂度为 O(2^n), Permutations时间复杂度是 O(n!)

Subset

```python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, idx, tempList, res):
        if len(tempList) == len(nums):
            res.append(tempList)
            return
        for i in range(idx, len(nums)):
            # 如果给定数组中有重复字符，不在同一位置重复尝试同一字符
            if i>idx and nums[i]==num[i-1]:
                continue
            # 
            self.helper(nums, i+1, tempList+nums[i], res)

```

Permutations
```python
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        # if has duplicated
        # self.helper2(nums, [], set(), res)
        return res

    def helper(self, nums, tempList, res):
        if len(tempList) == len(nums):
            res.append(tempList)
            return
        for i in range(len(nums)):
            if nums[i] in tempList:
                continue
            self.helper(nums, tempList+[nums[i]], res)

    # if has duplicated
    def helper2(self, nums, tempList, visited, res):
        if len(tempList) == len(nums):
            res.append(tempList)
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            if i>0 and nums[i] == nums[i-1] and i-1 in visited:
                continue
            visited.add(i)
            self.helper(nums, tempList+[nums[i]], visited, res)
            visited.remove(i)
```

