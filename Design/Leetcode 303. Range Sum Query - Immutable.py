class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]*(len(nums)+1)
        self.sums[0] = 0
        for i in range(1,len(nums)+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]
        

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]