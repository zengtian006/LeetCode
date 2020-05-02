class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.dic[number] = len(self.nums)
        self.nums.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.nums)):
            diff = value - self.nums[i]
            if diff in self.dic and self.dic[diff] != i:
                return True
        return False