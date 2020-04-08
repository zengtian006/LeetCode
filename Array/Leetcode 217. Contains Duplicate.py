class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            dic[num] = dic.get(num,0)+1
        return False

# O(1) 读写 考虑hashtable, set