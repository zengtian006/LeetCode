class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0<nums[i] <=len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
                
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]!=i+1:
                return i+1
        return len(nums)+1

        #堆排序 以[3,4,-1,1] 举例 第一轮遍历下来， 结果应该是[1,-1,3,4]， 1，3，4 都在应该在的位置上，只有-1 不对，所以输出2