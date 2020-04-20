class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums)-2
        while idx>=0:
            if nums[idx]<nums[idx+1]:
                break
            idx-=1
        if idx < 0:
            nums.sort()
            return
        
        nextIdx = idx+1
        while nextIdx<len(nums) and nums[nextIdx]>nums[idx]:
            nextIdx+=1
        
        #swap idx and nextIdx
        nums[idx], nums[nextIdx-1] = nums[nextIdx-1], nums[idx]
        nums[idx+1:] = nums[idx+1:][::-1]
        
        
# 1　　2　　7　　4　　3　　1   find 2 -> first element which is smaller that next element 
# 1　　2　　7　　4　　3　　1   find 3 -> smallest emlement which is larget that 2
# 1　　3　　7　　4　　2　　1   swap 2 and 3
# 1　　3　　[1　　2　　4　　7]   sort nums after 3