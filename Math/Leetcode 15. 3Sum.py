class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k>0 and nums[k] == nums[k-1]: continue
            target = -nums[k]
            i,j = k+1, len(nums)-1
            while i<j:
                if nums[i]+nums[j]<target:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                elif nums[i]+nums[j] == target:
                    res.append([nums[k],nums[i],nums[j]])
                    while i<j and nums[i] == nums[i+1]:
                        i+=1
                    while i<j and nums[j] == nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
        return res