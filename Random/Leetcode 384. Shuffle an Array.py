class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums_copy = self.nums[::]
        for i in range(len(nums_copy)):
            j = random.randint(0,i)
            nums_copy[i], nums_copy[j] = nums_copy[j], nums_copy[i]
        return nums_copy