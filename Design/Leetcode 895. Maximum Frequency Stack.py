class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        f = self.freq.get(x,0)+1
        self.freq[x] = f
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(x)
        
    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x