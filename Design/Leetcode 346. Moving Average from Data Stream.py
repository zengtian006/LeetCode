class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.q.popleft()
        self.q.append(val)
        return sum(self.q)/len(self.q)