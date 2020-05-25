class FreqStack:

    def __init__(self):
        self.dic = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        f =self.dic[x]+1
        self.freq[f].append(x)
        self.dic[x] = f
        self.max_freq = max(self.max_freq, f)
            
    def pop(self) -> int:
        x = self.freq[self.max_freq].pop()
        self.dic[x] -= 1
        if len(self.freq[self.max_freq]) == 0:
            self.max_freq -= 1
        return x