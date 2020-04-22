# Binary Search
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        res = []
        for num in nums2:
            idx = self.bs(num, nums1)
            if idx!=-1:
                res.append(num)
                nums1.pop(idx)
        return res

    def bs(self, target, nums):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1
        
#Two Pointer
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        return res
            
        
# HashTable
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic={}
        for num in nums1:
            dic[num] = dic.get(num,0)+1
        for num in nums2:
            if num in dic:
                res.append(num)
                dic[num]-=1
                if dic[num]==0:
                    del dic[num]
        return res