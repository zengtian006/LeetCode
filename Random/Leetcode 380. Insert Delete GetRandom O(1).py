class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.dic[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:        
        if val in self.nums:
            last_num, del_idx =self.nums[-1], self.dic[val]
            self.nums[del_idx], self.nums[-1] = self.nums[-1], self.nums[del_idx]
            self.nums.pop()
            self.dic[last_num] = del_idx
            del self.dic[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.sample(self.nums,1)[0]