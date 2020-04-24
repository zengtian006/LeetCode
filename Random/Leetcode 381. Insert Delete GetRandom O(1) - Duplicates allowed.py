class RandomizedCollection:

    def __init__(self):
        self.dic = collections.defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.dic[val].add(len(self.nums)-1)
        return len(self.dic[val]) == 1
        

    def remove(self, val: int) -> bool:
        if not self.dic[val]:
            return False
        idx_to_remove = self.dic[val].pop()
        last = self.nums[-1]
        self.nums[idx_to_remove] = last
        self.dic[last].add(idx_to_remove)
        self.dic[last].remove(len(self.nums)-1)
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)