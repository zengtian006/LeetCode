class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for k in range(n-3):
            if k>0 and nums[k] == nums[k-1]:
                continue
            for h in range(k+1,n-2):
                if h>k+1 and nums[h] == nums[h-1]:
                    continue
                new_tar = target-(nums[k]+nums[h])
                i, j = h+1, n-1
                while i < j:
                    sums = nums[i] + nums[j]
                    if sums == new_tar:
                        res.append([nums[k],nums[h],nums[i],nums[j]])
                        while i<j and nums[i] == nums[i+1]:
                            i+=1
                        while i<j and nums[j] == nums[j-1]:
                            j-=1
                        i+=1
                        j-=1
                    elif sums > new_tar:
                        j-=1
                    elif sums < new_tar:
                        i+=1
        return res