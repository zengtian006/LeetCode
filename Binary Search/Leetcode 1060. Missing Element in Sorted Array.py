# O(logn)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        rng = nums[-1] - nums[0] + 1 - len(nums)
        if rng <k:
            return nums[-1]+k-rng
        
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = left + (right-left)//2
            rng = nums[mid]-nums[left]-(mid-left)
            if rng == k:
                return nums[mid]-1
            elif rng > k:
                right = mid
            elif rng < k:
                k -= rng
                left = mid
        return nums[left]+k
        
# O(n)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        nxt = nums[0]+1
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                rng = nums[i+1] - nums[i] -1
                if rng >=k:
                    return nums[i]+k
                else:
                    k-= rng
        return nums[-1]+k